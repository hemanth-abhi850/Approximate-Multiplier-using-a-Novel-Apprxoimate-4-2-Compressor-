`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////
// Author Name: L Hemanth Krishna 
// Pursing   : Ph.D at IIT Mandi, Himachal Pradesh
// Contact   : lavatihemanthkrishna@gmail.com
// Address : Visakhapatnam, andhrapradesh
// Create Date:    12:15:21 04/04/2024

// Paper Title Name: Energy-Efficient Approximate Multiplier Design
//                   With Lesser Error Rate Using the Probability-Based
//                   Approximate 4:2 Compressor

// Module Name:    Multiplier Design using both exact and  approximate compressors

// Description: The below code is a 8x8 mulitplier using proposed approximate  compressor design-1

// Figure :5 in my research paper
//////////////////////////////////////////////////////////////////////////////////
module PB2P2(s1,a,b);
input [7:0]a,b;
output [15:0]s1;
wire [7:0] p0;
wire [8:1] p1;
wire [9:2] p2;
wire [10:3] p3;
wire [11:4] p4;
wire [12:5] p5;
wire [13:6] p6;
wire [14:7] p7;

wire [9:1] u,ca;
wire [14:1] q,s;
wire [8:1] x,y,z;
wire [7:1] r,t;

// 64 partial products

and a1(p0[0],a[0],b[0]);
and a2(p0[1],a[1],b[0]);
and a3(p0[2],a[2],b[0]);
and a4(p0[3],a[3],b[0]);
and a5(p0[4],a[4],b[0]);
and a6(p0[5],a[5],b[0]);
and a7(p0[6],a[6],b[0]);
and a8(p0[7],a[7],b[0]);


and a9(p1[1],a[0],b[1]);
and a10(p1[2],a[1],b[1]);
and a11(p1[3],a[2],b[1]);
and a12(p1[4],a[3],b[1]);
and a13(p1[5],a[4],b[1]);
and a14(p1[6],a[5],b[1]);
and a15(p1[7],a[6],b[1]);
and a16(p1[8],a[7],b[1]);


and a17(p2[2],a[0],b[2]);
and a18(p2[3],a[1],b[2]);
and a19(p2[4],a[2],b[2]);
and a20(p2[5],a[3],b[2]);
and a21(p2[6],a[4],b[2]);
and a22(p2[7],a[5],b[2]);
and a23(p2[8],a[6],b[2]);
and a24(p2[9],a[7],b[2]);


and a25(p3[3],a[0],b[3]);
and a26(p3[4],a[1],b[3]);
and a27(p3[5],a[2],b[3]);
and a28(p3[6],a[3],b[3]);
and a29(p3[7],a[4],b[3]);
and a30(p3[8],a[5],b[3]);
and a31(p3[9],a[6],b[3]);
and a32(p3[10],a[7],b[3]);


and a33(p4[4],a[0],b[4]);
and a34(p4[5],a[1],b[4]);
and a35(p4[6],a[2],b[4]);
and a36(p4[7],a[3],b[4]);
and a37(p4[8],a[4],b[4]);
and a38(p4[9],a[5],b[4]);
and a39(p4[10],a[6],b[4]);
and a40(p4[11],a[7],b[4]);


and a41(p5[5],a[0],b[5]);
and a42(p5[6],a[1],b[5]);
and a43(p5[7],a[2],b[5]);
and a44(p5[8],a[3],b[5]);
and a45(p5[9],a[4],b[5]);
and a46(p5[10],a[5],b[5]);
and a47(p5[11],a[6],b[5]);
and a48(p5[12],a[7],b[5]);


and a49(p6[6],a[0],b[6]);
and a50(p6[7],a[1],b[6]);
and a51(p6[8],a[2],b[6]);
and a52(p6[9],a[3],b[6]);
and a53(p6[10],a[4],b[6]);
and a54(p6[11],a[5],b[6]);
and a55(p6[12],a[6],b[6]);
and a56(p6[13],a[7],b[6]);


and a57(p7[7],a[0],b[7]);
and a58(p7[8],a[1],b[7]);
and a59(p7[9],a[2],b[7]);                     
and a60(p7[10],a[3],b[7]);
and a61(p7[11],a[4],b[7]);
and a62(p7[12],a[5],b[7]);
and a63(p7[13],a[6],b[7]);
and a64(p7[14],a[7],b[7]);

// approximate compressor

compres cmp1(u[1],ca[1],p0[5],p1[5],p2[5],p3[5]);
compres cmp2(u[2],ca[2],p0[6],p1[6],p2[6],p3[6]);
compres cmp3(u[3],ca[3],p0[7],p1[7],p2[7],p3[7]);
compres cmp4(u[4],ca[4],p4[7],p5[7],p6[7],p7[7]);
compres cmp5(u[5],ca[5],p0[3],p1[3],p2[3],p3[3]);
compres cmp6(u[6],ca[6],r[1],p2[4],p3[4],p4[4]);
compres cmp7(u[7],ca[7],u[1],t[1],p4[5],p5[5]);
compres cmp8(u[8],ca[8],u[2],r[2],p6[6],ca[1]);
compres cmp9(u[9],ca[9],u[3],u[4],ca[2],t[2]);

// Exact 4:2 compressor

compres5 cp1(x[1],y[1],z[1],p1[8],p2[8],p3[8],p4[8],ca[3]);
compres5 cp2(x[2],y[2],z[2],p2[9],p3[9],p4[9],p5[9],y[1]);
compres5 cp3(x[3],y[3],z[3],p3[10],p4[10],p5[10],p6[10],y[2]);
compres5 cp4(x[4],y[4],z[4],x[1],r[3],p7[8],ca[4],ca[9]);
compres5 cp5(x[5],y[5],z[5],x[2],r[4],z[1],t[3],y[4]);
compres5 cp6(x[6],y[6],z[6],x[3],p7[10],z[2],t[4],y[5]);
compres5 cp7(x[7],y[7],z[7],s[1],p7[11],z[3],y[3],y[6]);
compres5 cp8(x[8],y[8],z[8],q[1],p5[12],p6[12],p7[12],y[7]);

//Full Adder

FA fa1(s[1],q[1],p4[11],p5[11],p6[11]);
FA fa2(s[2],q[2],y[8],p6[13],p7[13]);
FA fa3(s[3],q[3],r[5],p2[2],t[6]);
FA fa4(s[4],q[4],u[5],t[5],q[3]);
FA fa5(s[5],q[5],u[6],ca[5],q[4]);
FA fa6(s[6],q[6],u[7],ca[6],q[5]);
FA fa7(s[7],q[7],u[8],ca[7],q[6]);
FA fa8(s[8],q[8],u[9],ca[8],q[7]);
FA fa9(s[9],q[9],x[5],z[4],t[7]);
FA fa10(s[10],q[10],x[6],z[5],q[9]);
FA fa11(s[11],q[11],x[7],z[6],q[10]);
FA fa12(s[12],q[12],x[8],z[7],q[11]);
FA fa13(s[13],q[13],s[2],z[8],q[12]);
FA fa14(s[14],q[14],p7[14],q[2],q[13]);

// Half Adder

HA ha1(r[1],t[1],p0[4],p1[4]);
HA ha2(r[2],t[2],p4[6],p5[6]);
HA ha3(r[3],t[3],p5[8],p6[8]);
HA ha4(r[4],t[4],p6[9],p7[9]);
HA ha5(r[5],t[5],p0[2],p1[2]);
HA ha6(r[6],t[6],p0[1],p1[1]);
HA ha7(r[7],t[7],x[4],q[8]);

assign s1={q[14],s[14],s[13],s[12],s[11],s[10],s[9],r[7],s[8],s[7],s[6],s[5],s[4],s[3],r[6],p0[0]};
endmodule

module HA(su,ca,a,b);
input a,b;
output su,ca;
xor g1(su,a,b);
and g2(ca,a,b);
endmodule

module FA(s,co,a,b,c);
input a,b,c;
output s,co;
assign s=(a^b^c);
assign co=((a&b) | (b&c) | (a&c));
endmodule

///Exact 4:2 COMPRESSOR

module compres5(sum,carry,cout,a,b,c,d,cin);
output sum,carry,cout;
input a,b,c,d,cin;
wire x;
FA u1(sum,carry,a,x,cin);
FA u2(x,cout,c,d,b);
endmodule

//proposed compressor design-2

module compres(sum,carry,a,b,c,d);
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
