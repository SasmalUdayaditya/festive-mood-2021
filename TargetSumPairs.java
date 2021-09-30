package fundamental_array;

import java.util.Scanner;

public class TargetSumPairs {
	public static void Target(int [] a, int n, int t)
	{
		for(int i=0;i<n-1;i++)
		{
			int temp = a[i];
			for(int j=i+1;j<n;j++)
			{
				if(a[j] == (t-temp))
				{
					 if(temp <= a[j])
						    System.out.println(temp+" and "+a[j]);
	                 else
	                        System.out.println(a[j]+" and "+temp);
				}
			}
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner sc  = new Scanner(System.in);
			int n = sc.nextInt();
			int[] arr = new int[n];
			for(int i=0;i<n;i++)
			{
				arr[i] = sc.nextInt();
			}
			int t = sc.nextInt();
			sc.close();
			Target(arr,n,t);
	}

}
