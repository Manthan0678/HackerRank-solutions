# Agricultural subsidies are offered by the Indian government to farmers for
# improving crop yields and benefiting them. To facilitate the farmers in
# finding the subsidy amount, develop a Python code to calculate the
# subsidy based on the crop the farmer grows. The farmers can grow one
# of these three types of crops: Rice, Wheat, or Maize. The program
# calculates and displays the type of crop, total subsidy based on the type
# of crop selected, along with the yield and market rate. Use menu driven
# approach to implement the same. Each crop has a different formula for
# calculating the subsidy:
# Rice: Subsidy= (Yield × Market Rate) +100
# Wheat: Subsidy= (Yield × Market Rate) +200
# Maize: Subsidy= (Yield × Market Rate) +300
# Input Format
# Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize
# Next Line to enter the Market Rate
# Next Line to enter the Yield
# Enter either Yes/No
# .
# Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize
# Next Line to enter the Market Rate
# Next Line to enter the Yield

# while True:
#     def function():
#         pathway = str(input("do you want to continue? (yes/no)")).strip()
#         if pathway == "yes":
#             continue
#         elif pathway =="no":
#             print("thankyou")
#             return
#         else:
#             print("invalid input")

#     crop = int(input("Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize"))
#     rate = int(input("enter the market rate for selected crop."))
#     yield_ = int(input("enter the yield"))
#     if crop == 1:
#         subsidy = (yield_ *rate) +100
#         print(subsidy)
#         function()
#     elif crop == 2:
#         subsidy = (yield_ *rate) +200
#         print(subsidy)
#         function()
#     elif crop == 3:
#         subsidy = (yield_ *rate) +300
#         print(subsidy)
#         function()
#     else:
#         print("enter valid input")
while True:
    print("Program to find the subsidy amount the farmer will get.")
    crop = int(input("Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize"))
    rate = int(input("enter the market rate for selected crop."))
    yield_ = int(input("enter the yield"))
    subsidy = (yield_ * rate) + (crop * 100)
    print(subsidy)
    pathway = str(input("do you want to continue? (yes/no)"))
    if pathway == "yes":
        continue
    elif pathway == "no":
        print("thankyou")
        break
    else:
        print("invalid input")




        
