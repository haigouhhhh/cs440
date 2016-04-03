import numpy as np

def main():
    hmm = open('Z:\\440\P3\sentence.hmm', 'r')
    obs = open('Z:\\440\P3\example2.obs', 'r')
    numberOf = hmm.readline()
    numberOfA = [0,0,0]
    numberOfA = numberOf.split()
    numberOfA = [int(l) for l in numberOfA]
    N = numberOfA[0]
    M = numberOfA[1]
    T = numberOfA[2]
    states = hmm.readline()
    statesA = ['','','','']
    snytax = states.split()
    observations = hmm.readline()
    observationsA = ['','','','','','','','']
    vocab = observations.split()
    hmm.readline()
    amat = []
    for i in range(0,4):
        a = hmm.readline()
        b = a.split()
        c = [float(l) for l in b]
        amat.append(c)
    hmm.readline()
    bmat = []
    for i in range(0,4):
        a = hmm.readline()
        b = a.split()
        c = [float(l) for l in b]
        bmat.append(c)
    hmm.readline()
    p = hmm.readline()
    p = p.split()
    pi = [float(l) for l in p]
    numsets = int(obs.readline())
    numobs = []
    observ = []
    for i in range (0, numsets):
        numobs.append(int(obs.readline()))
        a = obs.readline()
        b = a.split()
        observ.append(b)

    for h in range(0, numsets):
        alphas = np.zeros(shape=(numobs[h],N))
        print("alphas[0]: " + str(len(alphas[0])))
        for k in range(0,len(alphas[0])):
            alphas[0][k] = pi[k]*vocabmatch(observ[h][0],k, vocab, bmat)
        for t in range(1, numobs[h]):
            for j in range(0,N):
                alphabuf = 0
                for i in range(0,N):
                    alphabuf += alphas[t-1][i]*amat[i][j]
                alphas[t][j] = alphabuf*vocabmatch(observ[h][t], j, vocab, bmat);
        woo = alphas[numobs[h]-1][0] + alphas[numobs[h]-1][1] + alphas[numobs[h]-1][2] + alphas[numobs[h]-1][3]
        print("woo: " + str(woo))
        
    betas = np.zeros(shape=(numobs[h],N))
    for init in range(0,N):
        betas[numobs[h]-1][init] = 1
    #print("betas: " + str(betas))
    
    for t in range(numobs[h]-2, -1, -1):
        for i in range(0,N):
            betabuf = 0
            for j in range(0,N):
                betabuf += betas[t+1][j]*amat[i][j]*vocabmatch(observ[h][t+1],j,vocab,bmat)
            betas[t][i] = betabuf
    #print("betas:"  + str(betas))
    
    
    gammas = np.zeros(shape=(numobs[h],N))
    for t in range(0,numobs[h]):
        POlambda = 0
        for x in range(0,N):
            POlambda += alphas[t][x]*betas[t][x]
        for i in range(0,N):
            gammas[t][i] = (alphas[t][i]*betas[t][i])/POlambda
   # print("gammas: " + str(gammas))
    
    
    newpi = [0]*4
    #print ("newpi: " + str(newpi))
    newamat = np.zeros(shape=(N,N))
    b = len(bmat[0])
    #print("B: " + str(b))
    newbmat = np.zeros(shape=(N,b))
    c = numobs[h]-1
    xis = np.zeros(shape=(c,N,N))
    for t in range(0,c):
        s = 0
        for i in range(0,N):
            for j in range(0,N):
                s+= alphas[t][i]*amat[i][j]*vocabmatch(observ[h][t+1],j,vocab,bmat)*betas[t+1][j]
        for i in range(0,N):
            for j in range(0,N):
                xis[t][i][j] = (alphas[t][i]*amat[i][j]*vocabmatch(observ[h][t+1],j,vocab,bmat)*betas[t+1][j])/s
    
    #print("gammas: " + str(gammas))
    for i in range(0,N):
        newpi[i] =  gammas[0][i]
        
    for i in range(0,N):
        sumgamma = 0
        for x in range(0,c):
            sumgamma+= gammas[x][i]
        for j in range(0,N):
            sumxi = 0
            for t in range(0,c):
                sumxi+= xis[t][i][j]
            if (sumgamma == 0.0):
                newamat[i][j] = amat[i][j]
            else: newamat[i][j] = (sumxi/sumgamma)
    
    for j in range(0,N):
        for k in range(0,M):
            sumobk = 0
            sumgamma = 0
            for t in range(0,numobs[h]):
                if(observ[h][t] == vocab[k]):
                    sumobk += gammas[t][j];
                sumgamma += gammas[t][j]
            if (sumgamma == 0.0):
                newbmat[j][k] = bmat[j][k]
            else: newbmat[j][k] = (sumobk/sumgamma)
    
    for i in range(0,N):
        for j in range(0,N):
            amat[i].insert(j,newamat[i][j])
    for j in range(0,N):
        for k in range(0,M):
            bmat[j].insert(k,newbmat[j][k])
    pi = newpi
    
    #print("bmat: " + str(bmat))
    for k in range(0,N):
        alphas[0][k] = pi[k]*vocabmatch(observ[h][0],k,vocab,bmat)
    for t in range(1,numobs[h]):
        for j in range(0,N):
            alphabuf = 0
            for i in range(0,N):
                alphabuf += alphas[t-1][i]*amat[i][j]
            alphas[t][j] = alphabuf*vocabmatch(observ[h][t], j,vocab,bmat)

    woo = alphas[numobs[h]-1][0]+alphas[numobs[h]-1][1] + alphas[numobs[h]-1][2] + alphas[numobs[h]-1][3]
    #alphas[numobs[h]-1][0] + alphas[numobs[h]-1][1] + alphas[numobs[h]-1][2] + alphas[numobs[h]-1][3]
    print("woo: " + str(woo))
     
    f = open("optHMM.hmm", 'w')
    f.write(str(N) + ' ' + str(M) + ' ' + str(numobs[h]) + '\n')
    f.write("SUBJECT AUXILIARY PREDICATE OBJECT\n")
    f.write("kids robots do can play eat chess food\n")
    f.write("a:\n")
    for i in range (0, N):
        for j in range (0, N):
            f.write(str(amat[i][j]) + ' ')
        f.write('\n')
    f.write("b:\n")
    for j in range (0, N):
        for k in range (0, N):
            f.write(str(bmat[j][k]) + ' ')
        f.write('\n')
    f.write('pi:\n')
    for i in range (0, N):
        f.write(str(pi[i]) + ' ')
    f.close()          
                 
def vocabmatch(obs, state, vocab, bmat):
    for i in range (0, len(vocab)):
        #print bmat[state]
        if obs == vocab[i]:
            return bmat[state][i]
    return 0.0
 
                      
if __name__ == "__main__":
    main()
