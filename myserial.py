import serial
import threading
import time

class SerialManager:
    def __init__(self, port, baudrate):
        # timeout=1은 readline()이 데이터가 없을 때 무한 대기하는 것을 방지합니다.
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.running = True
        self.last_received = ""

        # 1. Thread 시작
        self.thread = threading.Thread(target=self._read_serial_loop, daemon=True)
        self.thread.start()

    def _read_serial_loop(self):
        with open("log.txt", "a", encoding="utf-8") as f:
            while self.running:
                if self.ser.in_waiting > 0:
                    # 데이터 읽기 및 디코딩
                    line = self.ser.readline().decode('utf-8', errors='replace').strip()
                    if line:
                        self.last_received = line
                        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {line}\n")
                        f.flush()
                time.sleep(0.01)

    # --- 추가된 Write 함수 ---
    def write_string(self, command):
        """명령어를 시리얼로 전송 (끝에 개행 문자 추가)"""
        if self.ser.is_open:
            # 명령어 뒤에 \n(엔터)를 붙여서 전송하는 경우가 많습니다.
            full_command = command + "\r\n"
            self.ser.write(full_command.encode('utf-8'))
            print(f"Sent command: {command}")
            self.ser.flush()
        else:
            print("Serial port is not open.")

    def wait_for_string(self, target_string, timeout):
        start_time = time.time()
        print(f"Waiting for '{target_string}' (timeout: {timeout}s)...")

        while time.time() - start_time < timeout:
            if self.last_received.find(target_string) != -1 :
                self.last_received = ""
                return True
            time.sleep(0.1)
        return False

    def close(self):
        self.running = False
        self.ser.close()

# --- 사용 예시 ---
if __name__ == "__main__":
    # 포트 번호는 환경에 맞게 수정하세요 (예: 'COM3' 또는 '/dev/ttyUSB0')
    sm = SerialManager('COM4', 115200)

    # 예: "OK"라는 문자열이 5초 안에 들어오는지 확인
    result = sm.wait_for_string("odroidc2 login:", 60.0)

    if result:
        print("Success: Found the string!")
    else:
        print("Failed: Timeout reached.")

    sm.write_string("revizes")
    time.sleep(1)
    sm.write_string("skdud.Wkd")

    time.sleep(3)

    sm.write_string("ls -al")

    time.sleep(5)

    sm.close()
