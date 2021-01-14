{-@ LIQUID "--totality" @-}
module Totality where

import Prelude hiding (head)

head (x:_) = x

-- head xs = case xs of
--   (x:_) -> x
--   []    -> patError "..."

-- patError :: {v:String | false} -> a






















nestcomment n ('{':'-':ss) | n>=0 = (("{-"++cs),rm)
                                  where (cs,rm) = nestcomment (n+1) ss
nestcomment n ('-':'}':ss) | n>0  = let (cs,rm) = nestcomment (n-1) ss
                                    in (("-}"++cs),rm)
nestcomment n ('-':'}':ss) | n==0 = ("-}",ss)
nestcomment n (s:ss)       | n>=0 = ((s:cs),rm)
                                  where (cs,rm) = nestcomment n ss
nestcomment n [] = ([],[])






















-- Local Variables:
-- flycheck-checker: haskell-liquid
-- End:

nestcomment :: Int -> String -> (String,String)

{-@ LIQUID "--no-termination" @-}
{-@ LIQUID "--diffcheck"      @-}
{-@ LIQUID "--short-names"    @-}
