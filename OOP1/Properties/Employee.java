public class Employee {
    // Private attributes
    private String name;
    private int age;
    private Double bonus; // Attribute ที่ไม่มีค่าเริ่มต้นใน constructor

    // Constructor
    public Employee(String name, int age) {
         //xyz
    }

    public Employee(String name) {
        //mno
    }

    Employee emp1= Employee("ABC",20);
    Employee emp2= Employee("ABC");
    Employee emp3= Employee(20);


        def __init__(self, name, age):
        self._name = name  # Attribute ที่กำหนดค่าใน constructor
        self._age = age    # Attribute ที่กำหนดค่าใน constructor
        self._bonus = None  # Attribute ที่ไม่มีค่าเริ่มต้นใน constructor

    // Getter สำหรับ 'name'
    public String getName() {
        System.out.println("Getting name");
        return this.name;
    }

    // Setter สำหรับ 'name'
    public void setName(String name) {
        if (name == null || !(name instanceof String)) {
            throw new IllegalArgumentException("Name must be a string");
        }
        System.out.println("Setting name");
        this.name = name;
    }

    // Getter สำหรับ 'age'
    public int getAge() {
        System.out.println("Getting age");
        return this.age;
    }

    // Setter สำหรับ 'age'
    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age must be a positive integer");
        }
        System.out.println("Setting age");
        this.age = age;
    }

    // Getter สำหรับ 'bonus' (Attribute ที่ไม่มีค่าเริ่มต้น)
    public Double getBonus() {
        if (this.bonus == null) {
            System.out.println("No bonus assigned yet");
        } else {
            System.out.println("Getting bonus");
        }
        return this.bonus;
    }

    // Setter สำหรับ 'bonus'
    public void setBonus(Double bonus) {
        if (bonus == null || bonus < 0) {
            throw new IllegalArgumentException("Bonus must be a positive number");
        }
        System.out.println("Setting bonus");
        this.bonus = bonus;
    }

    // Deleter สำหรับ 'bonus'
    public void deleteBonus() {
        System.out.println("Deleting bonus");
        this.bonus = null;
    }

    // Main method สำหรับทดสอบ
    public static void main(String[] args) {
        // การใช้งาน
        Employee emp = new Employee("Alice", 30);

        // เรียก getter ของ 'name' และ 'age'
        System.out.println(emp.getName()); // Output: Getting name \n Alice
        System.out.println(emp.getAge());  // Output: Getting age \n 30

        // เรียก getter ของ 'bonus' (ยังไม่มีค่า)
        System.out.println(emp.getBonus()); // Output: No bonus assigned yet \n null

        // เรียก setter ของ 'bonus' เพื่อกำหนดค่าใหม่
        emp.setBonus(5000.0); // Output: Setting bonus
        System.out.println(emp.getBonus()); // Output: Getting bonus \n 5000.0

        // เรียก deleter ของ 'bonus' เพื่อลบค่า
        emp.deleteBonus(); // Output: Deleting bonus
        System.out.println(emp.getBonus()); // Output: No bonus assigned yet \n null
    }
}