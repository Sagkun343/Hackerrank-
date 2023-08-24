def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    format = s[-2:]
    if format == "AM":
        if hour == 12:
            hour = 0
    elif format == "PM":
        if hour == 12:
            hour = 12
        else:
            hour += 12
    if hour < 10:
        hour = f"0{hour}"
    else:
        hour = f"{hour}"
    return f"{hour}{s[2:-2]}"

input = "12:21:23AM"
print(timeConversion(input))