total_aid <-read.csv("C:/Users/�漭��/Downloads/total aid.csv")
banking_finance <- read.csv("C:/Users/�漭��/Downloads/banking.csv")
education <- read.csv("C:/Users/�漭��/Downloads/Education.csv")
health <- read.csv("C:/Users/�漭��/Downloads/Health.csv")
pop_policy <- read.csv("C:/Users/�漭��/Downloads/Population Policies.csv")
government <- read.csv("C:/Users/�漭��/Downloads/Government & Civil Society.csv")
economic_infra <- read.csv("C:/Users/�漭��/Downloads/Economic Infrastructure & Services.csv")
social_infra <- read.csv("C:/Users/�漭��/Downloads/social Infrastructure & Services.csv")
library(readxl)
oda2 <- read_excel("C:/Users/�漭��/Downloads/oda2.xlsx")

merge_df <- merge(total_aid, banking_finance, by="LOCATION", all=TRUE)
merge_df <- merge(merge_df, education, by="LOCATION", all=TRUE)
merge_df <- merge(merge_df, health, by="LOCATION", all=TRUE)
merge_df <- merge(merge_df, pop_policy, by="LOCATION", all=TRUE)
merge_df <- merge(merge_df, government, by="LOCATION", all=TRUE)
merge_df <- merge(merge_df, economic_infra, by="LOCATION", all=TRUE)
merge_df <- merge(merge_df, social_infra, by="LOCATION", all=TRUE)
merge_df <- merge_df[c(1,3,5,7,9,11,13,15,17)]
merge_df

merge_df <- merge(merge_df, oda2, by="LOCATION", all=TRUE)
install.packages("openxlsx")
library(openxlsx)
write.xlsx(merge_df, file = "oda3.xlsx")

# ������ ��ü�� �������� �۾���
# oda3 = �߿� ���� ������
oda3 <- read_excel("C:/Users/�漭��/Downloads/oda3.xlsx", sheet=2)
# oda4 = �߿� ���� ����
oda4 <- read_excel("C:/Users/�漭��/Downloads/oda3.xlsx", sheet=3)

oda3 <- oda3[-9,] # DAC ������ ����
oda4

s_oda3 <- oda3  # ���ο� ������������ ����
s_oda3[, 3:14] <- scale(oda3[, 3:14])
s_oda4 <- oda4
s_oda4[, c(2,3,4,5,6,7,9,10,11,12,13,15,16,17,18,19,20,21,22,23,25,26)] <- scale(oda4[, c(2,3,4,5,6,7,9,10,11,12,13,15,16,17,18,19,20,21,22,23,25,26)])

# ��� Ȯ��
s_oda3 <- scale(oda3[,c(3:14)])
s_oda3 <- as.data.frame(s_oda3)
s_oda4 <- scale(oda4[,c(2,3,4,5,6,7,9,10,11,12,13,15,16,17,18,19,20,21,22,23,25,26)])
s_oda4 <- as.data.frame(s_oda4)
s_oda3 <- s_oda3[,-2]

#### 1
pca_result1 <- prcomp(s_oda3[,-c(1,14)], scale. = F)
pca_result1
summary(pca_result1)
plot(pca_result1, type = "l")


pca_result1_2d <- predict(pca_result1, newdata = s_oda3[,-c(1,14)])
plot(pca_result1_2d[,1], pca_result1_2d[,2], col = "blue", pch = 19, cex=0.7,
     xlab = "PC1", ylab = "PC2", main = "PCA Result 1 - 2D Projection", xlim=c(-2,2), ylim=c(-2,2))
biplot(pca_result1, scale = 0, xlim=c(-2,2), ylim=c(-2,2))
result1 <- pca_result1_2d[,c(1,2)]
plot(result1[,1], result1[,2])
result1_filtered <- result1[result1[,1] >= -2 & result1[,1] <= 2 & result1[,2] >= -1 & result1[,2] <= 1, ]
plot(result1_filtered[,1], result1_filtered[,2])
# 39 -> 35���� �� (���� ���� : 39 �̱� 13 ������ 20 �Ϻ� 36 ������)


hclust_result1 <- hclust(dist(result1_filtered), method = "average")
num_clusters <- 3
cluster_assignments1 <- cutree(hclust_result1, num_clusters)
table(cluster_assignments1)

result1_filtered <- data.frame(
    PC1 = c(-1.18949308, 0.23330586, -0.94305213, -0.88732388, -1.34651322, 1.34528259, 0.09720116, -1.29926748, -0.64601846, -0.56146337, 
            -1.40479253, -0.73050695, 0.88154032, -1.29199150, -1.13054422, -1.16992284, -1.26316339, -0.39937506, 0.56789351, -1.36827605, 
            -1.50884626, -1.14780227, -1.35336979, -1.44434287, 0.13745437, 0.87405073, -1.13767994, -0.94383859, -1.18296661, -1.36743340, 
            0.15450212, -1.33143156, -1.46466551, -1.46951396, 0.19771352),
    PC2 = c(-0.20616730, -0.34535693, 0.03027627, -0.09577404, -0.35959885, 0.17371277, 0.32968687, -0.26960972, 0.09083124, -0.35338529, 
            -0.05590605, 0.49745030, 0.28134122, -0.48239382, -0.19815750, -0.27355544, -0.55384099, -0.26687844, 0.11782722, -0.25428313, 
            0.44100015, -0.21672259, -0.35234022, 0.07681238, 0.22304706, -0.30869407, 0.04017002, -0.33296742, -0.43999462, 0.22237866, 
            -0.33601512, -0.36238656, 0.33890206, 0.22099894, -0.69651415),
    cluster_assignments1 = c(1,1,2,2,1,3,2,1,2,1,2,2,3,1,1,1,1,1,3,1,1,1,2,3,2,1,1,2,1,1,2)
)

# ��� Ȯ��
result1_filtered
plot(result1_filtered$PC1, result1_filtered$PC2, col=result1_filtered$cluster_assignments1, xlab="PC1", ylab="PC2")
abline(h=0)
abline(v=0)
plot(hclust_result1, main = "Dendrogram")
# �ѱ��� 19��, �ѱ��� ������ ���� : 13�� ���� 26�� �븣���� 6�� ĳ����

#### 2
pca_result2 <- prcomp(s_oda4, scale. = F)
pca_result2
summary(pca_result2)
plot(pca_result2, type = "l")


pca_result2_2d <- predict(pca_result2, newdata = s_oda4)
plot(pca_result2_2d[,1], pca_result2_2d[,2], col = "blue", pch = 19, cex=1.3,
     xlab = "PC1", ylab = "PC2", main = "PCA Result 2 - 2D Projection")
biplot(pca_result1, scale = 0)
result2 <- pca_result2_2d[,c(1,2)]

result2_filtered <- result2[result2[,1] >= -4, ]

plot(result2_filtered[,1], result2_filtered[,2])
# 2�� �� (���� ���� : 7 DEU 28 USA)


hclust_result2 <- hclust(dist(result2_filtered), method = "average")
num_clusters <- 3
cluster_assignments2 <- cutree(hclust_result2, num_clusters)
table(cluster_assignments2)

# ���ο� ������������ �����
cluster_num <- c(1, 2, 2, 2, 2, 1, 2, 1, 1, 3, 2, 1, 1, 2, 1, 1, 3, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1)

# ���ο� ������������ �����
new_df <- data.frame(PC1 = result2_filtered[, 1], PC2 = result2_filtered[, 2], clusternum = cluster_num)

# ��� Ȯ��
print(new_df)

# ��� Ȯ��
plot(new_df$PC1, new_df$PC2, col=new_df$clusternum, xlab="PC1", ylab="PC2")

plot(hclust_result2, main = "Dendrogram")
# �ѱ��� 19��, �ѱ��� ������ ���� : 9�� ������ 4�� ĳ���� 14�� �밡�� 26�� ���ι�Ű�� 15�� ���Ϸ���



### �׷� ���������� ���缺 : �ѱ� / �Ϻ� / ����ũ ~ ���еǴ� �׷� �� Ư¡ (Ŭ������ 1, 2���� �� �� ������ ��)
### �ѱ��� ���� : ĳ���� ~ �ѱ��� ��Ȱ��ǥ/���强/�������� ���� ������ ĳ������ oda ��å�� ���� ��� ���� ã�ƺ���.





