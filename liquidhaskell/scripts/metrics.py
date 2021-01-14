#!/usr/bin/python

from collections import defaultdict
from datetime import datetime
import os
import re
import string
import subprocess
import sys

benchmarks = {
    'benchmarks/text-0.11.2.3': [ 'Data/Text.hs'
                                , 'Data/Text/Array.hs'
                                , 'Data/Text/Encoding.hs'
                                , 'Data/Text/Foreign.hs'
                                , 'Data/Text/Fusion.hs'
                                , 'Data/Text/Fusion/Size.hs'
                                , 'Data/Text/Internal.hs'
                                , 'Data/Text/Lazy.hs'
                                , 'Data/Text/Lazy/Builder.hs'
                                , 'Data/Text/Lazy/Encoding.hs'
                                , 'Data/Text/Lazy/Fusion.hs'
                                , 'Data/Text/Lazy/Internal.hs'
                                , 'Data/Text/Lazy/Search.hs'
                                , 'Data/Text/Private.hs'
                                , 'Data/Text/Search.hs'
                                , 'Data/Text/Unsafe.hs'
                                , 'Data/Text/UnsafeChar.hs' ],

    'benchmarks/bytestring-0.9.2.1': [ 'Data/ByteString.T.hs'
                                     , 'Data/ByteString/Char8.hs'
                                     , 'Data/ByteString/Fusion.T.hs'
                                     , 'Data/ByteString/Internal.hs'
                                     , 'Data/ByteString/Lazy.hs'
                                     # , 'Data/ByteString/LazyZip.hs'
                                     , 'Data/ByteString/Lazy/Char8.hs'
                                     , 'Data/ByteString/Lazy/Internal.hs'
                                     , 'Data/ByteString/Unsafe.hs' ],

    'benchmarks/vector-algorithms-0.5.4.2': [ 'Data/Vector/Algorithms/AmericanFlag.hs'
                                            , 'Data/Vector/Algorithms/Combinators.hs'
                                            , 'Data/Vector/Algorithms/Common.hs'
                                            , 'Data/Vector/Algorithms/Heap.hs'
                                            , 'Data/Vector/Algorithms/Insertion.hs'
                                            , 'Data/Vector/Algorithms/Intro.hs'
                                            , 'Data/Vector/Algorithms/Merge.hs'
                                            , 'Data/Vector/Algorithms/Optimal.hs'
                                            , 'Data/Vector/Algorithms/Radix.hs'
                                            , 'Data/Vector/Algorithms/Search.hs' ],

    'benchmarks/esop2013-submission': [ 'Base.hs', 'Splay.hs' ],

    'benchmarks/hscolour-1.20.0.0': [ 'Language/Haskell/HsColour.hs'
                                    , 'Language/Haskell/HsColour/ACSS.hs'
                                    , 'Language/Haskell/HsColour/Anchors.hs'
                                    , 'Language/Haskell/HsColour/ANSI.hs'
                                    , 'Language/Haskell/HsColour/Classify.hs'
                                    , 'Language/Haskell/HsColour/ColourHighlight.hs'
                                    , 'Language/Haskell/HsColour/Colourise.hs'
                                    , 'Language/Haskell/HsColour/CSS.hs'
                                    , 'Language/Haskell/HsColour/General.hs'
                                    , 'Language/Haskell/HsColour/HTML.hs'
                                    , 'Language/Haskell/HsColour/InlineCSS.hs'
                                    , 'Language/Haskell/HsColour/LaTeX.hs'
                                    , 'Language/Haskell/HsColour/MIRC.hs'
                                    , 'Language/Haskell/HsColour/Options.hs'
                                    , 'Language/Haskell/HsColour/Output.hs'
                                    , 'Language/Haskell/HsColour/TTY.hs' ],

    'benchmarks/xmonad': [ 'XMonad/StackSet.hs' ],

    'include': [ 'GHC/List.lhs' ],

    '.': [ 'benchmarks/base-4.5.1.0/Data/List.hs' ]
}

def time(fn):
    start = datetime.now()
    with open(fn+'.log', 'w') as out:
        subprocess.call(['liquid', '--smtsolver', 'z3mem', fn], stdout=out, stderr=out)
    return (datetime.now() - start).total_seconds()

def errors(fn):
    with open(fn+'.log') as fd:
        log = fd.readlines()
    unsafes = [l for l in log if l.startswith('**** UNSAFE:')]
    return unsafes

def sloc(scripts,fn):
    return int(subprocess.check_output(
        '%s/haskell_count %s | tail -n1' % (scripts, fn), shell=True))

def lines(anns):
    return sum(map(lambda x:(1+x.count('\n')), anns))

def recs(fn):
    out = subprocess.check_output('liquid-count-binders %s 2>/dev/null' % fn, shell=True)
    return [int(n) for n in re.findall('(\d+)', out)]

def find(rx, str):
    return [(str[a.start():(3+string.find(str,"@-}", a.start()))])
            for a in list(re.finditer(rx, str))]

qualif_re = '{-@ qualif'
other = 'import|include|invariant|embed|Decrease|LAZYVAR|Strict|Lazy'
other_re = '{-@ (%s)' % other
spec_re = '{-@ (?!(%s|qualif|LIQUID))' % other
dec_re = '{-@ Decrease'
div_re = '{-@ (Strict|Lazy)'
wit_re = '{- LIQUID WITNESS'
mod_re = '^module ([\w\.]+)'

def combine(x, y):
    return {k:x[k] + y[k] for k in y.keys()}

def texify(fn, metrics):
    return '\\texttt{%s} & %d & %d / %d & %d / %d & %d / %d & %d & %d & %d & %d & %d \\\\\n' % (
        fn, metrics['sloc'], metrics['specs'], metrics['specs_lines'],
        metrics['others'], metrics['others_lines'],
        metrics['qualifs'], metrics['qualifs_lines'],
        metrics['funs'], metrics['recfuns'], metrics['divs'],
        metrics['hints'], metrics['time'])

def texify_term(fn, metrics):
    return '\\texttt{%s} & %d & %d & %d & %d & %d & %d & %d \\\\\n' % (
        fn, metrics['sloc'], metrics['errs'],
        metrics['funs'], metrics['recfuns'], metrics['divs'],
        metrics['hints'], metrics['time'])

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == '--only-term':
        print 'ONLY COLLECTING TERMINATION DATA!'
        colformat = '|l|rr|rrrr|r|'
        headers = ['Module', 'LOC', 'Err', 'Fun', 'Rec', 'Div', 'Hint', 'Time']
        pptex = texify_term
    else:
        colformat = '|l|rrrr|rrrr|r|'
        headers = ['Module', 'LOC', 'Specs', 'Annot', 'Qualif',
                   'Fun', 'Rec', 'Div', 'Hint', 'Time']
        pptex = texify
    results = {}
    pwd = os.getcwd()
    for d, fs in benchmarks.iteritems():
        os.chdir(d)
        results[d] = {}
        for fn in fs:
            print fn
            f_res = {}
            f_res['time'] = time(fn)
            f_res['sloc'] = sloc(os.path.join(pwd,'scripts'),fn)
            [fs,rs,rfs] = recs(fn)
            f_res['funs'] = fs
            f_res['recs'] = rs
            f_res['recfuns'] = rfs

            errs = set(errors(fn))
            import pprint
            pprint.pprint(errs)
            f_res['errs'] = len(errs)

            str = (open(fn, 'r')).read()
            mod = re.search(mod_re, str, re.M).group(1)

            specs = find(spec_re, str)
            f_res['specs'] = len(specs)
            f_res['specs_lines'] = lines(specs)

            qualifs = find(qualif_re, str)
            f_res['qualifs'] = len(qualifs)
            f_res['qualifs_lines'] = lines(qualifs)

            others = find(other_re, str)
            f_res['others'] = len(others)
            f_res['others_lines'] = lines(others)

            f_res['divs'] = len(re.findall(div_re, str))
            f_res['hints'] = len(re.findall(wit_re, str)) + len(re.findall(dec_re, str))
            results[d][mod] = f_res

        os.chdir(pwd)

    with open('metrics.tex', 'w') as out:
        out.write('\\begin{tabular}{%s}\n' % colformat)
        out.write('\\hline\n')
        out.write(' & '.join('\\textbf{%s}' % h for h in headers) + '\\\\\n')
        out.write('\\hline\\hline\n')
        totals = defaultdict(int)
        for d, fs in results.iteritems():
            dirtotals = defaultdict(int)
            for fn, metrics in sorted(fs.iteritems()):
                out.write(pptex(fn, metrics))
                dirtotals = combine(dirtotals, metrics)
            out.write(pptex(d, dirtotals))
            out.write('\\hline\n\n')
            totals = combine(totals, dirtotals)
        out.write(pptex('Total', totals))
        out.write('\\hline\n\\end{tabular}\n')

if __name__ == '__main__':
    main()
