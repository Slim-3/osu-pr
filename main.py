import json
import challonge
import consts



def main():
    challonge.set_credentials(consts.USER_NAME, consts.CHALLONGE_KEY)
    tournament = challonge.tournaments.show("ost_11_2020")


    # for i in data:
    #     print("Name:" + i["participant"]["name"] + "\t\t Final Rank: " + str(i["participant"]["final_rank"]))

if __name__ == '__main__':
    main()