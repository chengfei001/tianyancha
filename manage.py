import os


def main():
    f = open('company_list', 'r')
    for obj in f:
        command = 'scrapy crawl index -a company_name=%s' % obj
        print(command)
        # p = os.popen(command)
        os.system(command)


if __name__ == '__main__':
    main()