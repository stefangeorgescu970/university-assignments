function [L,U]=doolittle(A)
	[n,~]=size(A);
	I=eye(n);
	L=I;
	for k=1:n-1
		t=zeros(n,1);
		t(k+1:n)=A(k+1:n,k)./A(k,k);
		e=zeros(1,n);
		e(k)=1;
		A=(I-t*e)*A;
		L=L*(I+t*e);
	end
	U=A;
end
