def printValidOption():
    print("\nPlease enter a valid option.\n")
def getEntertainmentValueRating():
    finished=""
    while finished not in['y','n','q']:
        finished=input("\nDid you finish the book? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
        if finished=='q':
            return -1
        elif finished == 'n':
            return 1
        elif finished == 'y':
            force=""
            while force not in ['y','n','q']:
                force=input("\nDid you force yourself to finish this though? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if force =='q':
                    return -1
                elif force =='y':
                    return 2
                elif force=='n':
                    interesting=""
                    while interesting not in ['y','n','q']:
                        interesting=input("\nDid you find the book interesting? Type 'Y' if yes or 'N' if not really. Type 'Q' to quit\nAnswer: ").lower()
                        if interesting =='q':
                            return -1
                        elif interesting=='n':
                            return 3
                        elif interesting =='y':
                            intense=""
                            while intense not in ["y","n","q"]:
                                intense=input("\nDid you feel intense emotions (either happy or sad or angry) while reading? Type 'Y' if yes or 'N' if not really. Type 'Q' to quit\nAnswer: ").lower()
                                if intense == "q":
                                    return -1
                                elif intense == "n":
                                    return 4
                                elif intense =="y":
                                    return 5
                                printValidOption()
                        printValidOption()
                printValidOption()
        printValidOption()

def getPlotRating():
    problematic=""
    while problematic not in['y','n','q']:
        problematic=input("\nDid it contain problematic themes/messages? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
        if problematic=='q':
            return -1
        elif problematic == 'y':
            return 1
        elif problematic == 'n':
            interesting=""
            while interesting not in ['y','k','n','q']:
                interesting=input("\nWas the plot interesting? Type 'Y' if yes, 'K' if kinda, or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if interesting =='q':
                    return -1
                elif interesting =='n':
                    return 2
                elif interesting=='k':
                    return 3
                elif interesting=='y':
                    loopholes=""
                    while loopholes not in ['y','n','q']:
                        loopholes=input("\nDid it contain obvious loopholes/story gaps? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if loopholes =='q':
                            return -1
                        elif loopholes=='n':
                            return 5
                        elif loopholes =='y':
                            return 4
                        printValidOption()
                printValidOption()
        printValidOption()
        
def getCharacterRating():
    interesting=""
    while interesting not in['y','n','q']:
        interesting=input("\nWere any of the characters interesting. Type 'Y' if yes, 'N' if no, or 'Q' to quit\nAnswer: ").lower()
        if interesting=='q':
            return -1
        elif interesting == 'n':
           return 1
        elif interesting == 'y':
            other=""
            while other not in ['y','n','q']:
                other=input("\nWere other characters beside main character interesting? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if other =='q':
                    return -1
                elif other =='n':
                    return 2
                elif other=='y':
                    ooc=""
                    while ooc not in ['y','n','q']:
                        ooc=input("\nDid the main character feel OOC sometimes? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if ooc =='q':
                            return -1
                        elif ooc =='y':
                            return 3
                        elif ooc =='n':
                            developed=""
                            while developed not in ['y','n','q']:
                                developed=input("\nWere the characters well-developed and well-utilized? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                                if developed=="q":
                                    return -1
                                elif developed=="n":
                                    return 4
                                elif developed=="y":
                                    return 5
                        printValidOption()
                printValidOption()
        printValidOption()
        
def getWritingRating():
    grammatical_error=""
    while grammatical_error not in['y','n','q']:
        grammatical_error=input("\nDid it contain a lot of grammatical errors? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
        if grammatical_error=='q':
            return -1
        elif grammatical_error == 'y':
            return 1
        elif grammatical_error == 'n':
            pacing=""
            while pacing not in ['y','n','q']:
                pacing=input("\nWas the pacing too slow/fast for you? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if pacing =='q':
                    return -1
                elif pacing =='y':
                    return 2
                elif pacing=='n':
                    awkward=""
                    while awkward not in ['y','n','q']:
                        awkward=input("\nDid some parts feel awkwardly written? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if awkward =='q':
                            return -1
                        elif awkward =='y':
                            return 3
                        elif awkward =='n':
                            flawless=""
                            while flawless not in ['y','n','q']:
                                flawless=input("\nWould you say the writing is >=90\'%' flawless? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                                if flawless=='q':
                                    return -1
                                elif flawless =='n':
                                    return 4
                                elif flawless =='y':
                                    return 5
                                printValidOption()
                        printValidOption()
                printValidOption()
        printValidOption()
        
def getSubjectiveRating():
    recommend=""
    while recommend not in['y','n','q']:
        recommend=input("\nWill you recommend this to others? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
        if recommend=='q':
            return -1
        elif recommend == 'n':
            chance=""
            while chance not in ['y','n','q']:
                chance=input("\nWill you give this another chance in the future? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if chance =='q':
                    return -1
                elif chance =='n':
                    return 1
                elif chance=='y':
                    return 2
                printValidOption()
        elif recommend == 'y':
            remember=""
            while remember not in ['y','n','q']:
                remember=input("\nDo you think you will still remember most of this after 5 years? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if remember =='q':
                    return -1
                elif remember =='n':
                    return 3
                elif remember=='y':
                    spend=""
                    while spend not in ['y','n','q']:
                        spend=input("\nWould you keep a physical copy of this book? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if spend =='q':
                            return -1
                        elif spend =='n':
                            return 4
                        elif spend =='y':
                            return 5
                        printValidOption()
                printValidOption()
        printValidOption()                 
def bookRater():
    movie_title=input("Let's start! First off, what book are you rating today?\nAnswer: ")
    overall_rating=0
    entertainment_value_rating=getEntertainmentValueRating()
    if entertainment_value_rating<1:
        print("\nQuitting....\n")
        return
    plot_rating=getPlotRating()
    if plot_rating<1:
        print("\nQuitting....\n")
        return
    character_rating = getCharacterRating()
    if character_rating<1:
        print("\nQuitting....\n")
        return
    writing_rating=getWritingRating()
    if character_rating<1:
        print("\nQuitting....\n")
        return
    subjective_rating=getSubjectiveRating()
    if subjective_rating<1:
        print("\nQuitting....\n")
        return
    # Entertainment value = 50% Plot: 30% Characters: 10% Writing: 5% Recommendability/Rereadability: 5%
    overall_rating=(entertainment_value_rating*1)+(plot_rating*0.6)+(character_rating*0.2)+(writing_rating*0.1)+(subjective_rating*0.1)
    print("\nFinished! Your rating for "+movie_title+" is "+str(overall_rating)+"/10.\n")
    
bookRater()