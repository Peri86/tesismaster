/*
  main_betweenness.c
  $LastChangedDate: 2009-03-13 17:16:40 +0100 (Fri, 13 Mar 2009) $
  $Revision: 177 $
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include "graph.h"

int
main(int argc, char **argv)
{
  char *netF;
  FILE *infile=NULL;
  struct node_gra *net=NULL;
  struct node_gra *p=NULL;

  /*
    ---------------------------------------------------------------------------
    Command line parameters
    ---------------------------------------------------------------------------
  */
  if (argc < 2) {
    printf("\nUse: betweenness.out net_file\n\n");
    return;
  }
  netF = argv[1];

  /*
    ---------------------------------------------------------------------------
    Build the network
    ---------------------------------------------------------------------------
  */
  infile = fopen(netF, "r");
  net = FBuildNetwork(infile, 0, 0, 0, 1);
  fclose(infile);

  /*
    ---------------------------------------------------------------------------
    Calculate betweenness
    ---------------------------------------------------------------------------
  */
  CalculateNodeBetweenness(net);

  /*
    ---------------------------------------------------------------------------
    Output results and finish
    ---------------------------------------------------------------------------
  */
  p = net;
  while ((p = p->next) != NULL)
    printf("%s %d %g\n", p->label, CountLinks(p), p->dvar1);
  RemoveGraph(net);
  return 0;
}
