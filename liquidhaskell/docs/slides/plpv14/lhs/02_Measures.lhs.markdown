
 {#measures}
============

Measuring Data Types
--------------------

<div class="hidden">


<pre><span class=hs-linenum>11: </span><span class='hs-keyword'>module</span> <span class='hs-conid'>Measures</span> <span class='hs-keyword'>where</span>
<span class=hs-linenum>12: </span><span class='hs-keyword'>import</span> <span class='hs-conid'>Prelude</span> <span class='hs-varid'>hiding</span> <span class='hs-layout'>(</span><span class='hs-layout'>(</span><span class='hs-varop'>!!</span><span class='hs-layout'>)</span><span class='hs-layout'>,</span> <span class='hs-varid'>length</span><span class='hs-layout'>)</span>
<span class=hs-linenum>13: </span><span class='hs-keyword'>import</span> <span class='hs-conid'>Language</span><span class='hs-varop'>.</span><span class='hs-conid'>Haskell</span><span class='hs-varop'>.</span><span class='hs-conid'>Liquid</span><span class='hs-varop'>.</span><span class='hs-conid'>Prelude</span>
<span class=hs-linenum>14: </span>
<span class=hs-linenum>15: </span><span class='hs-definition'>length</span>      <span class='hs-keyglyph'>::</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>Int</span>
<span class=hs-linenum>16: </span><span class='hs-layout'>(</span><span class='hs-varop'>!</span><span class='hs-layout'>)</span>         <span class='hs-keyglyph'>::</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>Int</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>a</span>
<span class=hs-linenum>17: </span><span class='hs-definition'>insert</span>      <span class='hs-keyglyph'>::</span> <span class='hs-conid'>Ord</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>=&gt;</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span>
<span class=hs-linenum>18: </span><span class='hs-definition'>insertSort</span>  <span class='hs-keyglyph'>::</span> <span class='hs-conid'>Ord</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>=&gt;</span> <span class='hs-keyglyph'>[</span><span class='hs-varid'>a</span><span class='hs-keyglyph'>]</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span>
</pre>

</div>

Measuring Data Types 
====================

Recap
-----

1. <div class="fragment">**Refinements:** Types + Predicates</div>
2. <div class="fragment">**Subtyping:** SMT Implication</div>

<!--

---   -----------------------   ---  -------------------------
 1.      **Refinement Types**    :   Types + Predicates
 2.             **Subtyping**    :   SMT / Logical Implication 
---   -----------------------   ---  -------------------------

-->


Example: Lists 
--------------

<div class="hidden">


<pre><span class=hs-linenum>48: </span><span class='hs-keyword'>infixr</span> <span class='hs-varop'>`C`</span>
</pre>

</div>

<br>


<pre><span class=hs-linenum>56: </span><span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>=</span> <span class='hs-conid'>N</span> 
<span class=hs-linenum>57: </span>         <span class='hs-keyglyph'>|</span> <span class='hs-conid'>C</span> <span class='hs-varid'>a</span> <span class='hs-layout'>(</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span><span class='hs-layout'>)</span>
</pre>

Example: Length of a List 
-------------------------


<pre><span class=hs-linenum>64: </span><span class='hs-keyword'>{-@</span> <span class='hs-varid'>measure</span> <span class='hs-varid'>llen</span>  <span class='hs-keyglyph'>::</span> <span class='hs-layout'>(</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>Int</span>
<span class=hs-linenum>65: </span>    <span class='hs-varid'>llen</span> <span class='hs-layout'>(</span><span class='hs-conid'>N</span><span class='hs-layout'>)</span>      <span class='hs-keyglyph'>=</span> <span class='hs-num'>0</span>
<span class=hs-linenum>66: </span>    <span class='hs-varid'>llen</span> <span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-varid'>x</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>1</span> <span class='hs-varop'>+</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span>  <span class='hs-keyword'>@-}</span>
</pre>

<br>

<div class="fragment">
LiquidHaskell *strengthens* data constructor types
 <div/>
<pre><span class=hs-linenum>74: </span><span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>where</span> 
<span class=hs-linenum>75: </span>  <span class='hs-conid'>N</span> <span class='hs-keyglyph'>::</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>0</span><span class='hs-layout'>}</span>
<span class=hs-linenum>76: </span>  <span class='hs-conid'>C</span> <span class='hs-keyglyph'>::</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> 
<span class=hs-linenum>77: </span>         <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>1</span> <span class='hs-varop'>+</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span><span class='hs-layout'>}</span>
</pre>
</div>

Measures Are Uninterpreted
--------------------------

 <br>
<pre><span class=hs-linenum>85: </span><span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>where</span> 
<span class=hs-linenum>86: </span>  <span class='hs-conid'>N</span> <span class='hs-keyglyph'>::</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>0</span><span class='hs-layout'>}</span>
<span class=hs-linenum>87: </span>  <span class='hs-conid'>C</span> <span class='hs-keyglyph'>::</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> 
<span class=hs-linenum>88: </span>         <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>1</span> <span class='hs-varop'>+</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span><span class='hs-layout'>}</span>
</pre>

<br>

`llen` is an *uninterpreted function* in SMT logic

Measures Are Uninterpreted
--------------------------

In SMT, [uninterpreted function](http://fm.csl.sri.com/SSFT12/smt-euf-arithmetic.pdf) `f` obeys *congruence* axiom:

`forall x y. (x = y) => (f x) = (f y)`

<br>

<div class="fragment">
All other facts about `llen` asserted at *fold* and *unfold*
</div>

Measures Are Uninterpreted
--------------------------

All other facts about `llen` asserted at *fold* and *unfold*

<br>

<div class="fragment">
**Fold**<br>
<pre><span class=hs-linenum>117: </span><span class='hs-definition'>z</span> <span class='hs-keyglyph'>=</span> <span class='hs-conid'>C</span> <span class='hs-varid'>x</span> <span class='hs-varid'>y</span> <span class='hs-comment'>-- z :: {v | llen v = 1 + llen y}</span>
</pre>
</div>

<br>

<div class="fragment">
**Unfold**<br>
<pre><span class=hs-linenum>125: </span><span class='hs-keyword'>case</span> <span class='hs-varid'>z</span> <span class='hs-keyword'>of</span> 
<span class=hs-linenum>126: </span>  <span class='hs-conid'>N</span>     <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>e1</span> <span class='hs-comment'>-- z :: {v | llen v = 0}</span>
<span class=hs-linenum>127: </span>  <span class='hs-conid'>C</span> <span class='hs-varid'>x</span> <span class='hs-varid'>y</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>e2</span> <span class='hs-comment'>-- z :: {v | llen v = 1 + llen y}</span>
</pre>
</div>


Measured Refinements
--------------------

Now, we can verify:

<br>


<pre><span class=hs-linenum>140: </span><span class='hs-keyword'>{-@</span> <span class='hs-varid'>length</span>      <span class='hs-keyglyph'>::</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>(</span><span class='hs-conid'>EqLen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-keyword'>@-}</span>
<span class=hs-linenum>141: </span><a class=annot href="#"><span class=annottext>forall a. x1:(L a) -&gt; {VV : (Int) | (VV == (llen x1)) &amp;&amp; (VV &gt;= 0)}</span><span class='hs-definition'>length</span></a> <span class='hs-conid'>N</span>        <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>x1:(Int#) -&gt; {x2 : (Int) | (x2 == (x1  :  int))}</span><span class='hs-num'>0</span></a>
<span class=hs-linenum>142: </span><span class='hs-definition'>length</span> <span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-keyword'>_</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>{x2 : (Int) | (x2 == (1  :  int))}</span><span class='hs-num'>1</span></a> <a class=annot href="#"><span class=annottext>x1:(Int) -&gt; x2:(Int) -&gt; {x4 : (Int) | (x4 == (x1 + x2))}</span><span class='hs-varop'>+</span></a> <span class='hs-layout'>(</span><a class=annot href="#"><span class=annottext>forall a. x1:(L a) -&gt; {VV : (Int) | (VV == (llen x1)) &amp;&amp; (VV &gt;= 0)}</span><span class='hs-varid'>length</span></a> <a class=annot href="#"><span class=annottext>{x2 : (L a) | (x2 == xs)}</span><span class='hs-varid'>xs</span></a><span class='hs-layout'>)</span>
</pre>

<div class="fragment">

<br>

Where `EqLen` is a type alias:


<pre><span class=hs-linenum>152: </span><span class='hs-keyword'>{-@</span> <span class='hs-keyword'>type</span> <span class='hs-conid'>EqLen</span> <span class='hs-conid'>Xs</span> <span class='hs-keyglyph'>=</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-conid'>Nat</span> <span class='hs-keyglyph'>|</span> <span class='hs-varid'>v</span> <span class='hs-keyglyph'>=</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-conid'>Xs</span><span class='hs-layout'>)</span><span class='hs-layout'>}</span> <span class='hs-keyword'>@-}</span>
</pre>

</div>

List Indexing Redux
-------------------

We can type list indexed lookup:

<br>


<pre><span class=hs-linenum>165: </span><span class='hs-keyword'>{-@</span> <span class='hs-layout'>(</span><span class='hs-varop'>!</span><span class='hs-layout'>)</span>      <span class='hs-keyglyph'>::</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>(</span><span class='hs-conid'>LtLen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>@-}</span>
<span class=hs-linenum>166: </span><span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-varid'>x</span> <span class='hs-keyword'>_</span><span class='hs-layout'>)</span>  <a class=annot href="#"><span class=annottext>forall a.
x1:(L a) -&gt; {VV : (Int) | (VV &gt;= 0) &amp;&amp; (VV &lt; (llen x1))} -&gt; a</span><span class='hs-varop'>!</span></a> <span class='hs-num'>0</span> <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>{VV : a | (VV == x)}</span><span class='hs-varid'>x</span></a>
<span class=hs-linenum>167: </span><span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-keyword'>_</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-varop'>!</span> <span class='hs-varid'>i</span> <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>(L {VV : a | (x &lt;= VV)})</span><span class='hs-varid'>xs</span></a> <a class=annot href="#"><span class=annottext>forall a.
x1:(L a) -&gt; {VV : (Int) | (VV &gt;= 0) &amp;&amp; (VV &lt; (llen x1))} -&gt; a</span><span class='hs-varop'>!</span></a> <span class='hs-layout'>(</span><a class=annot href="#"><span class=annottext>{x2 : (Int) | (x2 &gt;= 0)}</span><span class='hs-varid'>i</span></a> <a class=annot href="#"><span class=annottext>x1:(Int) -&gt; x2:(Int) -&gt; {x4 : (Int) | (x4 == (x1 - x2))}</span><span class='hs-comment'>-</span></a> <a class=annot href="#"><span class=annottext>{x2 : (Int) | (x2 == (1  :  int))}</span><span class='hs-num'>1</span></a><span class='hs-layout'>)</span>
<span class=hs-linenum>168: </span><span class='hs-keyword'>_</span>        <span class='hs-varop'>!</span> <span class='hs-keyword'>_</span> <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>{x1 : [(Char)] | false} -&gt; {VV : a | false}</span><span class='hs-varid'>liquidError</span></a> <a class=annot href="#"><span class=annottext>{x3 : [(Char)] | ((len x3) &gt;= 0) &amp;&amp; ((sumLens x3) &gt;= 0)}</span><span class='hs-str'>"never happens!"</span></a>
</pre>

<br>

Where `LtLen` is a type alias:


<pre><span class=hs-linenum>176: </span><span class='hs-keyword'>{-@</span> <span class='hs-keyword'>type</span> <span class='hs-conid'>LtLen</span> <span class='hs-conid'>Xs</span> <span class='hs-keyglyph'>=</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-conid'>Nat</span> <span class='hs-keyglyph'>|</span> <span class='hs-varid'>v</span> <span class='hs-varop'>&lt;</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-conid'>Xs</span><span class='hs-layout'>)</span><span class='hs-layout'>}</span> <span class='hs-keyword'>@-}</span>
</pre>


List Indexing Redux
-------------------

Now we can type list indexed lookup:

 <br>
<pre><span class=hs-linenum>186: </span><span class='hs-keyword'>{-@</span> <span class='hs-layout'>(</span><span class='hs-varop'>!</span><span class='hs-layout'>)</span>      <span class='hs-keyglyph'>::</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>(</span><span class='hs-conid'>LtLen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>@-}</span>
<span class=hs-linenum>187: </span><span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-varid'>x</span> <span class='hs-keyword'>_</span><span class='hs-layout'>)</span>  <span class='hs-varop'>!</span> <span class='hs-num'>0</span> <span class='hs-keyglyph'>=</span> <span class='hs-varid'>x</span>
<span class=hs-linenum>188: </span><span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-keyword'>_</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-varop'>!</span> <span class='hs-varid'>i</span> <span class='hs-keyglyph'>=</span> <span class='hs-varid'>xs</span> <span class='hs-varop'>!</span> <span class='hs-layout'>(</span><span class='hs-varid'>i</span> <span class='hs-comment'>-</span> <span class='hs-num'>1</span><span class='hs-layout'>)</span>
<span class=hs-linenum>189: </span><span class='hs-keyword'>_</span>        <span class='hs-varop'>!</span> <span class='hs-keyword'>_</span> <span class='hs-keyglyph'>=</span> <span class='hs-varid'>liquidError</span> <span class='hs-str'>"never happens!"</span>
</pre>

<br>

<a href="http://goto.ucsd.edu:8090/index.html#?demo=HaskellMeasure.hs" target= "_blank">Demo:</a> 
What if we *remove* the precondition?

Multiple Measures
-----------------

LiquidHaskell allows *many* measures for a type


Multiple Measures 
-----------------

**Example:** Nullity of a `List` 


<pre><span class=hs-linenum>209: </span><span class='hs-keyword'>{-@</span> <span class='hs-varid'>measure</span> <span class='hs-varid'>isNull</span> <span class='hs-keyglyph'>::</span> <span class='hs-layout'>(</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>Prop</span>
<span class=hs-linenum>210: </span>    <span class='hs-varid'>isNull</span> <span class='hs-layout'>(</span><span class='hs-conid'>N</span><span class='hs-layout'>)</span>      <span class='hs-keyglyph'>=</span> <span class='hs-varid'>true</span>
<span class=hs-linenum>211: </span>    <span class='hs-varid'>isNull</span> <span class='hs-layout'>(</span><span class='hs-conid'>C</span> <span class='hs-varid'>x</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-varid'>false</span>           <span class='hs-keyword'>@-}</span>
</pre>

<br>

<div class="fragment">

 LiquidHaskell **strengthens** data constructors
<pre><span class=hs-linenum>219: </span><span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>where</span> 
<span class=hs-linenum>220: </span>  <span class='hs-conid'>N</span> <span class='hs-keyglyph'>::</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span> <span class='hs-conop'>:</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-layout'>(</span><span class='hs-varid'>isNull</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span><span class='hs-layout'>}</span>
<span class=hs-linenum>221: </span>  <span class='hs-conid'>C</span> <span class='hs-keyglyph'>::</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-layout'>(</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>|</span> <span class='hs-varid'>not</span> <span class='hs-layout'>(</span><span class='hs-varid'>isNull</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span><span class='hs-layout'>}</span>
</pre>

</div>

Multiple Measures
-----------------

LiquidHaskell *conjoins* data constructor types:

 <br>
<pre><span class=hs-linenum>232: </span><span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>where</span> 
<span class=hs-linenum>233: </span>  <span class='hs-conid'>N</span> <span class='hs-keyglyph'>::</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span>  <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>0</span> 
<span class=hs-linenum>234: </span>              <span class='hs-varop'>&amp;&amp;</span> <span class='hs-layout'>(</span><span class='hs-varid'>isNull</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-layout'>}</span>
<span class=hs-linenum>235: </span>  <span class='hs-conid'>C</span> <span class='hs-keyglyph'>::</span> <span class='hs-varid'>a</span> 
<span class=hs-linenum>236: </span>    <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> 
<span class=hs-linenum>237: </span>    <span class='hs-keyglyph'>-&gt;</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span>  <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span> <span class='hs-keyglyph'>=</span> <span class='hs-num'>1</span> <span class='hs-varop'>+</span> <span class='hs-layout'>(</span><span class='hs-varid'>llen</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> 
<span class=hs-linenum>238: </span>              <span class='hs-varop'>&amp;&amp;</span> <span class='hs-varid'>not</span> <span class='hs-layout'>(</span><span class='hs-varid'>isNull</span> <span class='hs-varid'>v</span><span class='hs-layout'>)</span>          <span class='hs-layout'>}</span>
</pre>

Multiple Measures
-----------------

Unlike [indexed types](http://dl.acm.org/citation.cfm?id=270793) ...

<br>

+ <div class="fragment">Measures *decouple* properties from structures</div>
+ <div class="fragment">Support *multiple* properties over structures </div>
+ <div class="fragment">Enable  *reuse* of structures                 </div>

<br>

<div class="fragment">Invaluable in practice!</div>

Refined Data Constructors
-------------------------

Can *directly pack* properties inside data constructors

<div class="fragment">

<br>


<pre><span class=hs-linenum>266: </span><span class='hs-keyword'>{-@</span> <span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyglyph'>=</span> <span class='hs-conid'>N</span>
<span class=hs-linenum>267: </span>             <span class='hs-keyglyph'>|</span> <span class='hs-conid'>C</span> <span class='hs-layout'>(</span><span class='hs-varid'>x</span> <span class='hs-keyglyph'>::</span> <span class='hs-varid'>a</span><span class='hs-layout'>)</span> 
<span class=hs-linenum>268: </span>                 <span class='hs-layout'>(</span><span class='hs-varid'>xs</span> <span class='hs-keyglyph'>::</span> <span class='hs-conid'>L</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-varid'>x</span> <span class='hs-varop'>&lt;=</span> <span class='hs-varid'>v</span><span class='hs-layout'>}</span><span class='hs-layout'>)</span>  <span class='hs-keyword'>@-}</span>
</pre>

</div>

<div class="fragment">

<br>

Specifies *increasing* Lists 
</div>

Refined Data Constructors
-------------------------

**Example:** Increasing Lists, with strengthened constructors:

 <br>
<pre><span class=hs-linenum>286: </span><span class='hs-keyword'>data</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span> <span class='hs-keyword'>where</span>
<span class=hs-linenum>287: </span>  <span class='hs-conid'>N</span> <span class='hs-keyglyph'>::</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span>
<span class=hs-linenum>288: </span>  <span class='hs-conid'>C</span> <span class='hs-keyglyph'>::</span> <span class='hs-varid'>x</span><span class='hs-conop'>:</span><span class='hs-varid'>a</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-varid'>xs</span><span class='hs-conop'>:</span> <span class='hs-conid'>L</span> <span class='hs-layout'>{</span><span class='hs-varid'>v</span><span class='hs-conop'>:</span><span class='hs-varid'>a</span> <span class='hs-keyglyph'>|</span> <span class='hs-varid'>x</span> <span class='hs-varop'>&lt;=</span> <span class='hs-varid'>v</span><span class='hs-layout'>}</span> <span class='hs-keyglyph'>-&gt;</span> <span class='hs-conid'>L</span> <span class='hs-varid'>a</span>
</pre>

<br>

- <div class="fragment">LiquidHaskell *checks* property when *folding* `C`</div>
- <div class="fragment">LiquidHaskell *assumes* property when *unfolding* `C`</div>

Refined Data Constructors
-------------------------

<a href="http://goto.ucsd.edu:8090/index.html#?demo=HaskellInsertSort.hs" target= "_blank">Demo: Insertion Sort</a> (hover for inferred types) 


<pre><span class=hs-linenum>302: </span><a class=annot href="#"><span class=annottext>forall a. (Ord a) =&gt; [a] -&gt; (L a)</span><span class='hs-definition'>insertSort</span></a> <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>(a -&gt; (L a) -&gt; (L a)) -&gt; (L a) -&gt; [a] -&gt; (L a)</span><span class='hs-varid'>foldr</span></a> <a class=annot href="#"><span class=annottext>a -&gt; (L a) -&gt; (L a)</span><span class='hs-varid'>insert</span></a> <a class=annot href="#"><span class=annottext>{x3 : (L {VV : a | false}) | (((isNull x3)) &lt;=&gt; true) &amp;&amp; ((llen x3) == 0)}</span><span class='hs-conid'>N</span></a>
<span class=hs-linenum>303: </span>
<span class=hs-linenum>304: </span><a class=annot href="#"><span class=annottext>forall a. (Ord a) =&gt; a -&gt; (L a) -&gt; (L a)</span><span class='hs-definition'>insert</span></a> <a class=annot href="#"><span class=annottext>a</span><span class='hs-varid'>y</span></a> <span class='hs-layout'>(</span><span class='hs-varid'>x</span> <span class='hs-varop'>`C`</span> <span class='hs-varid'>xs</span><span class='hs-layout'>)</span> 
<span class=hs-linenum>305: </span>  <span class='hs-keyglyph'>|</span> <a class=annot href="#"><span class=annottext>{VV : a | (VV == y)}</span><span class='hs-varid'>y</span></a> <a class=annot href="#"><span class=annottext>x1:a -&gt; x2:a -&gt; {x2 : (Bool) | (((Prop x2)) &lt;=&gt; (x1 &lt;= x2))}</span><span class='hs-varop'>&lt;=</span></a> <a class=annot href="#"><span class=annottext>{VV : a | (VV == x)}</span><span class='hs-varid'>x</span></a>    <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>{VV : a | (VV == y)}</span><span class='hs-varid'>y</span></a> <a class=annot href="#"><span class=annottext>x1:{VV : a | (VV &gt;= y)}
-&gt; x2:(L {VV : a | (VV &gt;= y) &amp;&amp; (x1 &lt;= VV)})
-&gt; {x3 : (L {VV : a | (VV &gt;= y)}) | (((isNull x3)) &lt;=&gt; false) &amp;&amp; ((llen x3) == (1 + (llen x2)))}</span><span class='hs-varop'>`C`</span></a> <span class='hs-layout'>(</span><a class=annot href="#"><span class=annottext>{VV : a | (VV == x)}</span><span class='hs-varid'>x</span></a> <a class=annot href="#"><span class=annottext>x1:{VV : a | (VV &gt;= x) &amp;&amp; (VV &gt;= y)}
-&gt; x2:(L {VV : a | (VV &gt;= x) &amp;&amp; (VV &gt;= y) &amp;&amp; (x1 &lt;= VV)})
-&gt; {x3 : (L {VV : a | (VV &gt;= x) &amp;&amp; (VV &gt;= y)}) | (((isNull x3)) &lt;=&gt; false) &amp;&amp; ((llen x3) == (1 + (llen x2)))}</span><span class='hs-varop'>`C`</span></a> <a class=annot href="#"><span class=annottext>{x2 : (L {VV : a | (x &lt;= VV)}) | (x2 == xs)}</span><span class='hs-varid'>xs</span></a><span class='hs-layout'>)</span>
<span class=hs-linenum>306: </span>  <span class='hs-keyglyph'>|</span> <span class='hs-varid'>otherwise</span> <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>{VV : a | (VV == x)}</span><span class='hs-varid'>x</span></a> <a class=annot href="#"><span class=annottext>x1:{VV : a | (VV &gt;= x)}
-&gt; x2:(L {VV : a | (VV &gt;= x) &amp;&amp; (x1 &lt;= VV)})
-&gt; {x3 : (L {VV : a | (VV &gt;= x)}) | (((isNull x3)) &lt;=&gt; false) &amp;&amp; ((llen x3) == (1 + (llen x2)))}</span><span class='hs-varop'>`C`</span></a> <a class=annot href="#"><span class=annottext>forall a. (Ord a) =&gt; a -&gt; (L a) -&gt; (L a)</span><span class='hs-varid'>insert</span></a> <a class=annot href="#"><span class=annottext>{VV : a | (VV == y)}</span><span class='hs-varid'>y</span></a> <a class=annot href="#"><span class=annottext>{x2 : (L {VV : a | (x &lt;= VV)}) | (x2 == xs)}</span><span class='hs-varid'>xs</span></a>
<span class=hs-linenum>307: </span><span class='hs-definition'>insert</span> <span class='hs-varid'>y</span> <span class='hs-conid'>N</span>    <span class='hs-keyglyph'>=</span> <a class=annot href="#"><span class=annottext>{VV : a | (VV == y)}</span><span class='hs-varid'>y</span></a> <a class=annot href="#"><span class=annottext>x1:{VV : a | (VV == y)}
-&gt; x2:(L {VV : a | (VV == y) &amp;&amp; (x1 &lt;= VV)})
-&gt; {x3 : (L {VV : a | (VV == y)}) | (((isNull x3)) &lt;=&gt; false) &amp;&amp; ((llen x3) == (1 + (llen x2)))}</span><span class='hs-varop'>`C`</span></a> <a class=annot href="#"><span class=annottext>{x3 : (L {VV : a | false}) | (((isNull x3)) &lt;=&gt; true) &amp;&amp; ((llen x3) == 0)}</span><span class='hs-conid'>N</span></a>    
</pre>

<br>

<div class="fragment">**Problem 1:** What if we need *both* [increasing and decreasing lists](http://web.cecs.pdx.edu/~sheard/Code/QSort.html)?</div>

Recap
-----

1. **Refinements:** Types + Predicates
2. **Subtyping:** SMT Implication
3. <div class="fragment">**Measures:** Strengthened Constructors</div>
    - <div class="fragment">*Decouple* structure & property, enable *reuse*</div>

