import pywhatkit

# Each minute whassappp cannon

print("Hello!! Your program has started. ENJOY SPAMMING!!")

#  Your message goes here.
Message = "TYPE YOUR MSG HERE"
Number = 'Type your number here with country code!!'
start_time = 1  # 24-hr format
end_time = 6  # 24-hr format
while start_time < end_time:
    for minute in range(60):
        pywhatkit.sendwhatmsg(Number, Message, start_time, minute, 10,
                              True, True)
    start_time += 1
