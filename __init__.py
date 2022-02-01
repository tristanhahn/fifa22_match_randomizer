import team_data_extractor
import match_randomizer


def main():
    league_exclusion_list = ["Mexico Liga MX (1)", "CONMEBOL Sudamericana", "Argentina Primera División (1)",
                             "Brazil Serie A (1)", "CONMEBOL Libertadores", "USA Major League Soccer (1)",
                             "Saudi Pro League (1)", "Brazil Serie A (1)"]
    match_randomizer.run_randomizer(rating_min=4, rating_max=5, exlusion_leagues=league_exclusion_list)


if __name__ == "__main__":
    main()
