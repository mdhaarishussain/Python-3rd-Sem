x=int(input("Enter x: "));
y=int(input("Enter y: "));
z=int(input("Enter z: "));
print("[Before Rotation]");
print("x: ",x);
print("y: ",y);
print("z: ",z);
c=z;
z=x;
x=y;
y=c;
print("[After Rotation]");
print("x: ",x);
print("y: ",y);
print("z: ",z);
