// Proposed 4:2 Compressor Design-1 %% Error rate 18.75 which means
//Three combinations are  wrong out of 16 combinations
// The Error Probability is 19/256


// Design-1 

module compressor(sum,carry,a,b,c,d);
input a,b,c,d;
output sum,carry;
wire [3:0]x;
wire [2:0]y;
wire t;
or g1(x[0],a,b),g2(x[2],c,d),g3(y[0],x[0],x[2]),g4(y[1],x[1],x[3]);
and g5(x[1],a,b),g6(x[3],c,d);
nand g7(y[2],x[0],x[2]);
or g8(t,y[1],y[2]);
and g9(sum, y[0],t);
not g10(carry,y[2]);
endmodule
