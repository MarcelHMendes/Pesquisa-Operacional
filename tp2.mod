var Y{1..9}, binary; 		#variables bh-regions
var X{1..9,1..9} , binary;	#variables facilities-regions 

param c{1..9} default 1;			# Implamtation costs
param f{1..9,1..9} default 1;     	# Facilitities cost


minimize z: sum{j in 1..9} c[j]* Y[j] + sum{k in 1..9, l in 1..9} f[k,l] * X[k,l];

subject to constraint{j in 1..9}:  sum{i in 1..9 } X[i,j] = 1;	#(1)
subject to constraint2{i in 1..9, j in 1..9}: 	X[i,j]<= Y[i];  #(2)
subject to constraint3: sum{i in 1..9} Y[i] = 3;  				#(6) máximo de facilidades disponíveis. 

data;

param : c := 
	1	3344
	2	4817
	3	3132
	4	5173
	5	5127
	6	5236	
	7	7176	
	8	4824	
	9	4408 ;

param f :	1	2	3	4	5	6	7	8	9	:=
	1		0	4	3	8	10	12	18	15	20	
	2		4	0	6 	7	10	5	16	13	19
	3		4	6	0	9	15	13	21	17	24
	4		8	7	9	0	6	5	12	10	17
	5		10	10	15	6	0	7	8	5	11
	6		2	5	13	5	7	0	11	11	16
	7		18	16	21	12	8	11	0	8	10
	8		15	13	17	10	5	11	8	0	7
	9		20	19	24	17	11	16	10	7	0 ;

end;
