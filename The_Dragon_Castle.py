print("----------------------------")
print("Welcome to the Dragon Castle")
print("----------------------------")
print('''
                __        _      
              _/  \    _(\(o     
             /     \  /  _  ^^^o 
            /   !   \/  ! '!!!v' 
           !  !  \ _' ( \____    
           ! . \ _!\   \===^\)   
            \ \_!  / __!         
             \!   /    \         
       (\_      _/   _\ )        
        \ ^^--^^ __-^ /(__       
         ^^----^^    "^--v'
  
  ''')

print("---------------------------------")
print()
print()

print("You have to answer three questions correctly in order to challenge the dragon.\n")
  
question1 = input("Are you ready? (Yes or No) ")
  
if question1 == "Yes":
  print()
  print("Well, let's get started. \n")

  print("----------------------\n")

  print("The Statue of Liberty was a gift to the United States from which European country ?")
  print()
  print("A. Belgium")
  print("B. Germany")    
  print("C. Spain")
  print("D. France")
  print()
  answer1 = input("What is your answer? (A, B, C, D) ")
  if answer1 == "D":
    print()
    print("✔ Good Job ✔")
    print()
    print("It's time for the second question\n")
    question2 = input("Are you ready? (Yes or No) ")
    if question2 == "Yes":
      print()
      print("----------------------\n")

      print("Which is the easiest way to tell the age of many trees?")
      print()
      print("A. To measure the width of the tree")
      print("B. To count the rings on the trunk")    
      print("C. To count the number of leaves")
      print("D. To measure the height of the tree")
      print()
      answer2 = input("What is your answer? (A, B, C, D) ")
      if answer2 == "B":
        print()
        print("✔ Well done ✔\n")
        
        print("It's time for the last question\n")
        question3 = input("Are you ready? (Yes or No) ")
        if question3 == "Yes":
          print()
          print("----------------------\n")

          print("What is the most visited tourist attraction in the world?")
          print()
          print("A. Eiffel Tower")
          print("B. Statue of Liberty")    
          print("C. Great Wall of China")
          print("D. Colosseum")
          print()
          answer3 = input("What is your answer? (A, B, C, D) ")
          if answer3 == "A":
            print()
            print("✔ Perfect ✔, you guessed all the quizzes.")
            print()
            question4 = input("Are you ready for the boss fight? (Yes or No) ")
            if question4 == "Yes":
              print()
              print("----------------------\n")
              
              print("************************ ▶ WARNING ◀ ************************")
              print()
              print("THE DRAGON IS READY TO HIT YOU WITH HIS FIREBALL.") 
              print()
              print("YOU HAVE FOUND A VERY SHARP PIECE OF METAL ON THE GROUND.")
              print()
              print("YOU HAVE A FEW SECONDS TO ACT.")
              print()
              print("************************ ▶ WARNING ◀ ************************")
              print('''
           .==.        .==.
           //`^\\      //^`\\
          // ^ ^\(\__/)/^ ^^\\
         //^ ^^ ^/6  6\ ^^ ^^\\
        //^ ^^ ^ ( .. ) ^ ^^^ \\
       // ^^ ^/\//v""v\\/\^ ^ ^\\
      // ^^/\/  / `~~` \  \/\^ ^\\
      \\^ /    / ,    , \    \^ //
       \\/    ( (      ) )    \//
        ^      \ \.__./ /      ^
               (((`  ')))
               
               ''')
              print(input("Press the ENTER key to continue "))
              print()
              print("WHAT IS THE DRAGON WEAK POINT?")
              print()
              print("A. WINGS")
              print("B. LEGS")    
              print("C. NECK")
              print("D. TAIL") 
              print()
              answer4 = input("What is your answer? (A, B, C, D) ")
              if answer4 == "C":
                print()
                print("✪ YOU DEFEATED THE DRAGON ✪")

              else:
                print()
                print("☠ You have been defeated by the dragon ☠")
            
          else:
            print()
            print("It's wrong, Game Over ✘")
      
      else:
        print()
        print("It's wrong, Game Over ✘")
        
    else:
      print()
      print("You are not ready, so you lost ✘")
      
  else:
    print()
    print("It's wrong, Game Over ✘")

else:
  print()
  print("You are not ready, so you lost ✘")