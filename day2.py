def is_report_safe(report: list[int]) -> bool:
    if report[0] == report[-1]: # must be unsafe
        return False
    diffs = [
        report[i] - report[i-1] if report[0] < report[-1] else report[i-1] - report[i]
        for i in range(1, len(report))
    ]
    return all(1 <= diff <= 3 for diff in diffs)


if __name__ == "__main__":
    num_safe = 0

    with open('day2.txt', 'r') as fp:
        for line in fp:
            report = [int(digit) for digit in line.split(' ')]
            if is_report_safe(report):
                num_safe += 1
            else:
                for i, _ in enumerate(report):
                    copyReport = report.copy()
                    copyReport.pop(i)
                    if is_report_safe(copyReport):
                        num_safe += 1
                        break
    print(num_safe)

