#include<Stdio.h>
int main()
{
int windowSize,totalframes,i;
int frames[50];
printf("Enter windowSize:");
scanf("%d",&windowSize);
printf("\n Enter number of frames to transmit:");
scanf("%d",&totalframes);
printf("\n Enter %d frames ",totalframes);
for(i=1;i<=totalframes;i++)
{
scanf("%d",&frames[i]);
}
printf("\n sliding window protocal simulation (Assuming NO frame Loss/ corruption) \n");
printf ("sends sends%d frames a a time and waits for acknowledgement.\n\n",windowSize);
for(i=1;i<=totalframes;i++)
{
printf("%d",frames[i]);
if(i% windowSize==0)
{
printf("\nAcknowlwdgement of above frames is received by sender\n\n");
}
}
if (totalframes % windowSize!=0)
{
printf("\nAcknowledgement of a aabove frames is received by sender\n");
}
return 0;
}