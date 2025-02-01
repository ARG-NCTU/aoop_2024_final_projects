from git_commit_count import get_commits_by_user
import argparse
import xlsxwriter
import os
import copy

def main():

    parser = argparse.ArgumentParser(description='Get commit counts by user from a git repository.')
    parser.add_argument('--repo', type=str, default='/home/arg/aoop_2024_final_projects', help='Path to the git repository.')
    parser.add_argument('--start_date', type=str, default='2024-09-29', help='Start date for commit count calculation. Format: YYYY-MM-DD', nargs='?')
    args = parser.parse_args()

    github_accounts = [
        ["Daniel47725812", "jjjerryc"],  
        ["kevinrayrayray", "Morgan119502", "billwang0517"],  
        ["hsuanyo7160", "WoodyLiang", "howard-shi55"],  
        ["ModernHuman0531", "jameshsu1973"],  
        ["Lian", "hac-ohmygod0193", "YunTin0628"],  
        ["lonea2005", "alan111511237", "mingzi9397"],  
        ["TTT426", "chenmax1016"],  
        ["OlafLin24", "charlie-ww"],  
        ["Lin-shao-an", "gdpps1028"],  
        ["bensonchen-del", "someone7414"],  
        ["lyj87", "TJKAI00"]
    ]

    # commits_by_users = [[] for _ in range(len(github_accounts))]
    commits_by_users = copy.deepcopy(github_accounts)

    for i, group in enumerate(commits_by_users):
        for j, student in enumerate(group):
            commits_by_users[i][j] = 0

    print(github_accounts)

    for sub_repo in os.listdir(args.repo):
        sub_repo_path = os.path.join(args.repo, sub_repo)

        # Iterate over the list of GitHub accounts
        for i, accounts in enumerate(github_accounts):
            for j, account in enumerate(accounts):
                commit_count = get_commits_by_user(sub_repo_path, account, args.start_date)
                if commit_count is not None:
                    commits_by_users[i][j] += commit_count

        # Print the commit counts for each user
        for i, accounts in enumerate(github_accounts):
            print(f"Group {i+1}:")
            for j, account in enumerate(accounts):
                if account == "":
                    continue
                print(f"User: {account}, Commit Count: {commits_by_users[i][j]}")

    # Export the commit counts to a xlsx file
    workbook = xlsxwriter.Workbook('commit_counts.xlsx')
    worksheet = workbook.add_worksheet('github_commit')
    worksheet.write(0, 0, "Group")
    worksheet.write(0, 1, "Group Member")
    worksheet.write(0, 2, "Group Member")
    worksheet.write(0, 3, "Group Member")
    for i, accounts in enumerate(github_accounts):
        worksheet.write(i+1, 0, f"Group {i+1}")
        for j, account in enumerate(accounts):
            if account == "":
                continue
            worksheet.write(i+1, j+1, f"{github_accounts[i][j]} : {commits_by_users[i][j]}")
    workbook.close()

if __name__ == '__main__':
    main()

