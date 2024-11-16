// Proposed 4:2 Compressor Design-2 %% Error rate 31.25 which means
// Five combinations are  wrong out of 16 combinations
// But Error probability is 13/256



// Design-2 

module compressor(sum,carry,a,b,c,d);
input a,b,c,d;
output sum,carry;
wire [3:0]x;
wire [2:0]y;
wire t;
or g1(x[0],a,b),g2(x[2],c,d),g3(y[0],x[0],x[2]),g4(y[1],x[1],x[3]);
and g5(x[1],a,b),g6(x[3],c,d),g7(y[2],x[0],x[2]);
nor g8(t,y[1],y[2]);
and g9(sum, y[0],t);
not g10(carry,t);
endmodule
