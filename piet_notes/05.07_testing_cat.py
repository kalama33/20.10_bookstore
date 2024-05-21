# 1. Make the test fail

WATER_HOURS = [8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]


def main():
    test_failed = False
    cat_controller = CatController()

    # cat_controller is my instance and should have the hourly_run method, which should give water

    # Test that water is only given each hour 8-11 and 13-19.
    for hour in range(0, 23):
        if hour in WATER_HOURS:
            if "Give water." not in cat_controller.hourly_run(hour):
                test_failed = True
        elif "Give water." in cat_controller.hourly_run(hour):
            test_failed = True

    # Test that the cat cage opened at 7:
    if "Open cat cage." not in cat_controller.hourly_run(7):
        test_failed = True

    return "All test ran successfully." if not test_failed else "Test failed"


# 2. Make the test pass
class CatController:
    def hourly_run(self, time):
        if time == 7:
            return "Open cat cage."
        elif time == 8:
            return "Give water."
        elif time == 12:
            return ""
        elif time == 17:
            return "Give water."
        elif time > 7 and time < 20:
            return "Give water."
        else:
            return "Let's sleep"


print(main())