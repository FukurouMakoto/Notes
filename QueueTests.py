import QueueImplementation

Movie_line = QueueImplementation.Queue()
print(f"Empty Queue; should return True. \nResult: {Movie_line.is_empty()}.")
print(f"Queue Size should be empty.\nResult: {Movie_line.size()}.")
print(f"Queue Peek should be empty. \nResult: {Movie_line.peek()}.")
print(f"Queue poll should be empty. \nResult: {Movie_line.poll()}.")
print("")
print("We're gonna add some stuff now.")
print("")
Movie_line.offer('Rachel')
Movie_line.offer('Karen')
Movie_line.offer('James')
print(f"We now have three people on line. Is_empty should return false. \nResult: {Movie_line.is_empty()}.")
print(f"Queue Size should return 3.\nResult: {Movie_line.size()}.")
print(f"First on the line should be Rachel. \nResult: {Movie_line.peek()}.")
Movie_line.poll() #Rachel
print("Rachel just got into the theater")
print(f"Next on line should be Karen. \nResult: {Movie_line.peek()}.")
print(f"We should now have two people on line. \nResult: {Movie_line.size()}.")
print("")
print("Oh fuck it's time for rush hour.")
print("")
Movie_line.offer('Sam')
Movie_line.offer('David')
Movie_line.offer('Michael')
Movie_line.offer('Jacob')
Movie_line.offer('Joseph')
print(f"Queue Size should return 7.\nResult: {Movie_line.size()}.")
print(f"First on line should be Karen. \nResult: {Movie_line.peek()}.")
print("Oh thank goodness the night shift arrived")
Movie_line.poll() #Karen
Movie_line.poll() #James
Movie_line.poll() #Sam
Movie_line.poll() #David
print(f"Next on line should be Michael. \nResult: {Movie_line.peek()}.")
print(f"We should now have three people on line. \nResult: {Movie_line.size()}.")
Movie_line.poll() #Michael
Movie_line.poll() #Jacob
Movie_line.poll() #Joseph
print(f"The front staff finally got thru everyone. Queue should be empty.")
print(f"Result: {Movie_line.size()}. \nIs_empty should return True. Result: {Movie_line.is_empty()}")