import team_data_extractor
import match_randomizer

def main():
    if team_data_extractor.check_if_extractor_already_run_today() == False:
        team_data_extractor.run_extractor()
        match_randomizer.run_randomizer(rating = 3.5)
    else:
        match_randomizer.run_randomizer(rating=3.5)

if __name__ == "__main__":
    main()