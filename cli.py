import argparse
from timemasterx.core import TimeMasterX

def main():
    parser = argparse.ArgumentParser(description="TimeMasterX CLI")
    parser.add_argument("--now", action="store_true", help="Afficher la date et l'heure actuelle")
    parser.add_argument("--add", nargs=4, type=int, metavar=("DAYS", "HOURS", "MINUTES", "SECONDS"), help="Time to add du temps")
    parser.add_argument("--date", type=str, help="Date to manipulate")
    parser.add_argument("--subtract", nargs=4, type=int, metavar=("DAYS", "HOURS", "MINUTES", "SECONDS"), help="Time to subtract")
    

    args = parser.parse_args()
    tm = TimeMasterX(args.date)

    if args.now:
        print(tm.now())
    if args.add:
        print(tm.add_time(*args.add))
    if args.subtract:
        print(tm.subtract_time(*args.subtract))

if __name__ == "__main__":
    main()
