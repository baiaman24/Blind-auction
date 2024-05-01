from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bid_dic ={}

def add_new_bid(name, bid_amount):
  bid_dic[name] = bid_amount

should_continue = True

while should_continue:
  name = input("What is your name?\n")
  bid = int(input("How much do you want to bid?\n$ "))
  add_new_bid(name, bid)
  next = input("Do you want to make new bid? Yes or No \n") 
  if next == "No":
    highest_bid = 0
    highest_bidder = ""
    for bidders in bid_dic:
      if bid_dic[bidders] > highest_bid:
        highest_bidder = bidders
        highest_bid = bid_dic[bidders]
    print(f"Highest bidder is {highest_bidder} with $ {highest_bid}")
    should_continue =False
  elif next == "Yes":
    clear()