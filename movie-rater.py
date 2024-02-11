def printValidOption():
    print("\nPlease enter a valid option.\n")
def getEntertainmentValueRating():
    finished=""
    while finished not in['y','n','q']:
        finished=input("\nDid you finish the movie/series? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
        if finished=='q':
            return -1
        elif finished == 'n':
            return 1
        elif finished == 'y':
            hooked=""
            while hooked not in ['y','k','n','q']:
                hooked=input("\nWere you hooked? Type 'Y' if yes, 'K' if kinda, or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if hooked =='q':
                    return -1
                elif hooked =='n':
                    return 2
                elif hooked=='k':
                    return 3
                elif hooked=='y':
                    rewatched=""
                    while rewatched not in ['y','n','q']:
                        rewatched=input("\nDid you rewatch some scenes just because you liked them or you were very intrigued? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if rewatched =='q':
                            return -1
                        elif rewatched=='n':
                            return 4
                        elif rewatched =='y':
                            return 5
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
        
def getActorRating():
    acting=""
    while acting not in['g','b','q']:
        acting=input("\nHow were the actors overall? Type 'G' if good or 'B' if bad. Type 'Q' to quit\nAnswer: ").lower()
        if acting=='q':
            return -1
        elif acting == 'b':
            main_actors=""
            while main_actors not in ['y','n','q']:
                main_actors=input("\nCan the main actors act? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if main_actors =='q':
                    return -1
                elif main_actors =='n':
                    return 1
                elif main_actors=='y':
                    return 2
                printValidOption()
        elif acting == 'g':
            awkward=""
            while awkward not in ['y','n','q']:
                awkward=input("\nDid some scenes feel awkward? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if awkward =='q':
                    return -1
                elif awkward =='y':
                    return 3
                elif awkward=='n':
                    natural=""
                    while natural not in ['y','n','q']:
                        natural=input("\nWas the acting very natural that you can't tell it's acting? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if natural =='q':
                            return -1
                        elif natural =='n':
                            return 4
                        elif natural =='y':
                            return 5
                        printValidOption()
                printValidOption()
        printValidOption()
        
def getCinematographyRating():
    low_budget=""
    while low_budget not in['y','n','q']:
        low_budget=input("\nDid the movie feel low-budget? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
        if low_budget=='q':
            return -1
        elif low_budget == 'y':
            transitions=""
            while transitions not in ['y','n','q']:
                transitions=input("\nWere the transitions tolerable? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if transitions =='q':
                    return -1
                elif transitions =='n':
                    return 1
                elif transitions=='y':
                    return 2
                printValidOption()
        elif low_budget == 'n':
            transitions=""
            while transitions not in ['y','n','q']:
                transitions=input("\nWere the transitions smooth? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                if transitions =='q':
                    return -1
                elif transitions =='n':
                    return 3
                elif transitions=='y':
                    shots=""
                    while shots not in ['y','n','q']:
                        shots=input("\nDid the shots made you feel emotions? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if shots =='q':
                            return -1
                        elif shots =='n':
                            return 4
                        elif shots =='y':
                            return 5
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
                        spend=input("\nWill you spend money to watch this again? Type 'Y' if yes or 'N' if no. Type 'Q' to quit\nAnswer: ").lower()
                        if spend =='q':
                            return -1
                        elif spend =='n':
                            return 4
                        elif spend =='y':
                            return 5
                        printValidOption()
                printValidOption()
        printValidOption()                 
def movieRater():
    movie_title=input("Let's start! First off, what's the movie/series you are rating today?\nAnswer: ")
    overall_rating=0
    entertainment_value_rating=getEntertainmentValueRating()
    if entertainment_value_rating<1:
        print("\nQuitting....\n")
        return
    plot_rating=getPlotRating()
    if plot_rating<1:
        print("\nQuitting....\n")
        return
    actor_rating = getActorRating()
    if actor_rating<1:
        print("\nQuitting....\n")
        return
    cinematography_rating=getCinematographyRating()
    if actor_rating<1:
        print("\nQuitting....\n")
        return
    subjective_rating=getSubjectiveRating()
    if subjective_rating<1:
        print("\nQuitting....\n")
        return
    # Entertainment value = 50% Plot: 25% Actors: 10% Cinematography: 5% Recommendability/Rewatchability: 10%
    overall_rating=(entertainment_value_rating*1)+(plot_rating*0.5)+(actor_rating*0.2)+(cinematography_rating*0.1)+(subjective_rating*0.2)
    print("\nFinished! Your rating for "+movie_title+" is "+str(overall_rating)+"/10.\n")
    
movieRater()