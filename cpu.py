class EnhancedCPU:
    def __init__(self):
        self.registers = [0] * 4  # 4 thanh ghi (registers)
        self.ios = 0  # IOS (Input/Output System), tương đương với Program Counter
        self.memory = [0] * 256  # Bộ nhớ (memory) với 256 ô nhớ
        self.flags = {"ZERO": False, "NEGATIVE": False}  # Thanh ghi dấu hiệu (flag register)

    def load_program(self, program):
        """Tải chương trình vào bộ nhớ"""
        for i in range(len(program)):
            self.memory[i] = program[i]

    def update_flags(self, result):
        """Cập nhật các flags sau mỗi phép toán"""
        self.flags["ZERO"] = (result == 0)
        self.flags["NEGATIVE"] = (result < 0)

    def execute(self):
        """Chạy các lệnh trong chương trình"""
        while self.ios < len(self.memory):
            opcode = self.memory[self.ios]  # Lệnh (opcode)
            
            if opcode == 0:  # Lệnh kết thúc (halt)
                print("Program halted.")
                break
            elif opcode == 1:  # Lệnh cộng (add)
                reg1 = self.memory[self.ios + 1]
                reg2 = self.memory[self.ios + 2]
                self.registers[reg1] += self.registers[reg2]
                self.update_flags(self.registers[reg1])
                self.ios += 3
            elif opcode == 2:  # Lệnh trừ (subtract)
                reg1 = self.memory[self.ios + 1]
                reg2 = self.memory[self.ios + 2]
                self.registers[reg1] -= self.registers[reg2]
                self.update_flags(self.registers[reg1])
                self.ios += 3
            elif opcode == 3:  # Lệnh lưu (load)
                reg = self.memory[self.ios + 1]
                value = self.memory[self.ios + 2]
                self.registers[reg] = value
                self.ios += 3
            elif opcode == 4:  # Lệnh nhân (multiply)
                reg1 = self.memory[self.ios + 1]
                reg2 = self.memory[self.ios + 2]
                self.registers[reg1] *= self.registers[reg2]
                self.update_flags(self.registers[reg1])
                self.ios += 3
            elif opcode == 5:  # Lệnh chia (divide)
                reg1 = self.memory[self.ios + 1]
                reg2 = self.memory[self.ios + 2]
                if self.registers[reg2] == 0:
                    print("Error: Division by zero!")
                    break
                self.registers[reg1] //= self.registers[reg2]
                self.update_flags(self.registers[reg1])
                self.ios += 3
            else:
                print(f"Unknown opcode {opcode} at address {self.ios}")
                break

            # In trạng thái các thanh ghi và flag sau mỗi lần thực thi
            print(f"IOS: {self.ios}, Registers: {self.registers}, Flags: {self.flags}")

# Ví dụ chương trình
program = [
    3, 0, 10,  # Lệnh lưu giá trị 10 vào thanh ghi 0
    3, 1, 20,  # Lệnh lưu giá trị 20 vào thanh ghi 1
    1, 0, 1,   # Lệnh cộng giá trị thanh ghi 1 vào thanh ghi 0
    4, 0, 1,   # Lệnh nhân thanh ghi 0 với thanh ghi 1
    5, 0, 1,   # Lệnh chia thanh ghi 0 cho thanh ghi 1
    0           # Lệnh kết thúc (halt)
]

# Tạo CPU và chạy chương trình
cpu = EnhancedCPU()
cpu.load_program(program)
cpu.execute()
