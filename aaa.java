class Hack1{
 void print1(){
  System.out.println("Good");}}
class Hack2{
 void print2(){
  System.out.println("Morning");}}
class Hack3 extends Hack1,Hack2{
 public static void main(String args[]){
   Hack3 obj=new Hack3(); 
   obj.msg();}}