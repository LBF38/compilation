abstract class AbstractClass {
  void abstractMethod();
  int abstractField;
  int anotherAbstractField;

  AbstractClass(this.abstractField, this.anotherAbstractField);
}

class Class {
  int field;

  Class(this.field);

  int method(int arg) {
    return arg;
  }
}
