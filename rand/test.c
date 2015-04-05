#include <stdlib.h>
#include <stdio.h>

struct reponse {
  unsigned int key0;
  unsigned int key1;
  unsigned int key2;
  unsigned int key3;
  unsigned int iv0;
  unsigned int iv1;
};


struct reponse rep;
static unsigned long int next = 1;

int rand(void) { // RAND_MAX assumed to be 32767
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}

void srand(unsigned int seed) {
    next = seed;
}




void bruteRand(unsigned int i){

  if(!(i % 1000000))
    printf("Palier : %d\n",i);
  srand(i);
  rep.key0 = rand();
  rep.key1 = rand();
  rep.key2 = rand();
  rep.key3 = rand();
  rep.iv0 = rand();
  rep.iv1 = rand();

}
int main(int argc, char *argv[]) {



  unsigned int IV_0 = 20146;
  unsigned int IV_1 = 31368;
  unsigned int i =  925307076;

  while(1){
    if((rep.iv0 == IV_0) & (rep.iv1 == IV_1))
      break;
    bruteRand(i);
    i++;
  }
  printf("--%d\n",i);
  printf("%d,%d,%d,%d,%d,%d\n",rep.key0,rep.key1,rep.key2,rep.key3,rep.iv0,rep.iv1);
}
