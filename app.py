#!/bin/python

import sys
import pocket

def main():

    # print('main')

    # pass file with api credentials
    # example:
    #   ./app.py -f ./credentials.json 


    # if sys.argv[1] == "-f":
    #     output_file = sys.argv[2]

    # pass api credentials manually
    # example:
    #   ./app.py -m 0000-0000-0000 0000-0000-0000 --get-all-data


    # if sys.argv[1] == "-m":
    #     consumer_key = sys.argv[2]
    #     access_token = sys.argv[3]
    #     if sys.argv[4] == "--get-all-data":
    #         pocket1 = pocket.Pocket(consumer_key, access_token)
    #         answer = pocket1.retrieve_all_data()
    #         print(answer)




    # Two modes
    # -m - manual - compose one liner with all credentials
    #       - return json with response
    # -a - automatic - pass json with credentials and other settings

    if sys.argv[1] == "-m":

        consumer_key = sys.argv[2]
        access_token = sys.argv[3]

        if sys.argv[4] == "--get-all-data":

            pocket_object = pocket.Pocket(consumer_key, access_token)

            if sys.argv[5] == "--pretty":

                all_data_pretty = pocket_object.retrieve_all_data("true")
                # return all_data
                # test purpose
                print(all_data_pretty)

            else:

                all_data_raw = pocket_object.retrieve_all_data("false")
                print(all_data_raw)

        if sys.argv[4] == "--get-by-tag":
            pass


if __name__ == "__main__":
    main()