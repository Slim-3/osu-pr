#import JSON
import challonge
import consts



def main():
    challonge.set_credentials(consts.USER_NAME, consts.CHALLONGE_KEY)
    tournament = challonge.tournaments.show("ost_11_2020")

    participant = sorted(challonge.participants.index(tournament["id"]), key=lambda i: i['final_rank'])

    print(tournament["name"]+ "\t")
    print("-" * len(tournament["name"]))
    print("{0:<15} Rank:".format("Name:"))
    for i in participant:
        print('{0[name]:<15} {0[final_rank]:d}'.format(i))

         #print("Name:" + i["participant"]["name"] + "\t\t Final Rank: " + str(i["participant"]["final_rank"]))
    print("-" * len(tournament["name"]))
if __name__ == '__main__':
    main()

