function x=gauss(A,b)
	n=length(b);
	for p=1:n-1
		[~,q]=max(abs(A(p:n,p)));
		q=q+p-1;
		A([p,q],:)=A([q,p],:);
		b([p,q])=b([q,p]);
		for i=p+1:n
			m=A(i,p)/A(p,p);
			A(i,:)=A(i,:)-m*A(p,:);
			b(i)=b(i)-m*b(p);
		end
	end
	x=backwardSub(A,b);
end
