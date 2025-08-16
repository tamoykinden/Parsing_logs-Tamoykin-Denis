from parse_args import par_args
from report import gen_rep

#Функция запуска
def main():
    args = par_args()
    report = gen_rep(args.file, args.report, args.date)

    print(report)

if __name__ == '__main__':
    main()