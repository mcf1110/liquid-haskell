
module IntAbsRef where

{-@ data Foo a <p :: Int -> Bool> = Foo { x::Int<p>}@-}

data Foo  a= Foo {x :: Int}
  
{-@ foo :: Foo <{\v -> v /= 1}> Int @-}
foo :: Foo Int
foo = Foo 1
