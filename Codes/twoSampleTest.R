fisher.test(cbind(c(1,9),c(11,3)),alternative = "less")

chisq.test(cbind(c(90,60,104,95),c(30,50,51,20),c(30,40,45,35)))


# 1_2 studying or not
chisq.test(cbind(c(1,8),c(11,4)),correct=TRUE)
fisher.test(cbind(c(1,8),c(11,4)))

# 1_1 teacher 
chisq.test(cbind(c(92,81),c(8,19)))
fisher.test(cbind(c(92,81),c(8,19)))

# 1_3_1 sex
chisq.test(cbind(c(9,7),c(70,68)),correct=TRUE)
fisher.test(cbind(c(9,7),c(70,68)))

  # 1_3_1 location
chisq.test(cbind(c(4,35),c(12,103)),correct=TRUE)
fisher.test(cbind(c(4,12),c(35,103)))

# 1_3_2 ways
chisq.test(cbind(c(7,57),c(5,43)),correct=TRUE)
fisher.test(cbind(c(7,57),c(5,43)))

# 2_1 drug
mcnemar.test(cbind(c(80,100),c(10,110)))

# 2_2 VTD
mcnemar.test(cbind(c(72,6),c(25,57)))

# 2_3 TD
mcnemar.test(cbind(c(59,6),c(16,80)))

x <- c(7,10,11,12,15,16,20,1,5,6)
y <- c(2,3,4,8,9,13,14,17,18,19)
wilcox.test(x, y, paired=F,correct = T,exact=F)

x <-c (42, 43, 45, 47, 49, 51, 53, 55, 57, 59)
y<-c(41, 44, 46, 48, 50, 52, 54, 56, 58, 60)
wilcox.test(x, y, paired=F,correct = T,exact=F)

2*(1-pnorm(1.96))
2*(1-pnorm(0.2645751311064591))

x<-c( 9.91,  9.25, 11.21 , 9.76 , 8.51 , 9.6,  10.2,   9.99 , 9.95 , 9.33) 
y<-c( 9.49, 10.7 ,  9.51, 10.99, 10.74, 10.32 ,10.49 , 9.57 ,10.6 ,  9.45)
wilcox.test(x, y, paired=F,correct = T,exact=F)

