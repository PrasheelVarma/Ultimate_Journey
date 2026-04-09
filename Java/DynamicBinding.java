abstract class DynamicBinding
{
 abstract void rose ();
}
class Abc extends DynamicBinding
{
   void rose()
   {
System.out.println("Roses are Beautiful");
   }
}
class Xyz extends DynamicBinding
{
   void rose()
   {
      System.out.println("Roses are many colors");

   }
}
class Pqr extends DynamicBinding
{
   void rose()
   {
      System.out.println("Roses give rosy smell");
      
   }
}


