class EmployeeData:
    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department


class PayCalculator:
    @staticmethod
    def __get_regular_hours():
        print("給与計算用の労働時間計算ロジック")

    def calculate_pay(self, employee_data: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee_data.name}の給与を計算しました")


class HourReporter:
    @staticmethod
    def __get_regular_hours():
        print("労働時間レポート用の労働時間計算ロジック_V2")
        # print("労働時間レポート用の労働時間計算ロジック")

    def report_hours(self, employee_data: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee_data.name}の労働時間をレポートしました")


class EmployeeRepository:
    @staticmethod
    def save(employee_data: EmployeeData):
        print(f"{employee_data.name}を保存しました")


if __name__ == "__main__":
    data = EmployeeData("鈴木", "開発")
    pay_calculator = PayCalculator()
    hour_reporter = HourReporter()

    print("経理部門")
    pay_calculator.calculate_pay(data)

    print("")
    print("人事部門")
    hour_reporter.report_hours(data)
