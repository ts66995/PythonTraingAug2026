tokens=25000
if tokens>50001:
    print("Use Large Large Model")
elif tokens>=10001 and tokens<=50000:
    print("Use Medium Context Model")
elif tokens<=10000:    
    print("Use Small Context Model")