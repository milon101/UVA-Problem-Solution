while True:
    n = int(input())
    if n == 0:
        break
    find = []
    replaceBy = []
    for i in range(n):
        w1 = input().strip()
        find.append(w1)
        w2 = input().strip()
        replaceBy.append(w2)
    line = input().strip()

    for i in range(n):
        while (line.find(find[i])>=0):
            line = line.replace(find[i], replaceBy[i])
    print (line)


##import java.io.BufferedReader;
##import java.io.IOException;
##import java.io.InputStreamReader;
##
##public class Main {
##
## public static void main(String[] args) throws IOException {
##  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
##  String line;
##  String[] find, replaceBy;
##  int i, caseNum;
##  while ((line = in.readLine()) != null) {
##   caseNum = Integer.parseInt(line);
##
##   if (caseNum == 0) {
##    System.exit(0);
##   }
##
##   find = new String[caseNum];
##   replaceBy = new String[caseNum];
##
##   for (i = 0; i < caseNum; i++) {
##    find[i] = line = in.readLine();
##    replaceBy[i] = line = in.readLine();
##   }
##
##   line = in.readLine();
##
##   for (i = 0; i < caseNum; i++) {
##    while (line.indexOf(find[i]) >= 0) {
##     line = line.replaceFirst(find[i], replaceBy[i]);
##    }
##   }
##
##   System.out.println(line);
##  }
## }
##}
