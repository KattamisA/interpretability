clear all
close all

%% Load and plot confidences
t=0:100:10000;
% img_names = ["panda", "F16_GT", "monkey",'zebra_GT'];
img_names = ["panda", "peacock", "F16_GT", "monkey",'zebra_GT','goldfish','whale','dolphin','spider','labrador'];
Confidence = zeros(101,size(img_names,2));
common = 'Adam/%s_ID%d_Normalised.txt';

ID = [2, 4, 8, 16, 32, 64];
Averaged= zeros(101,size(ID,2));
Std = zeros(101,size(ID,2));

%% Filling in the matrices
for j=1:size(ID,2)
    for i=1:size(img_names,2)
        path = sprintf(common,img_names(i),ID(j));
        s = load(path);
        Confidence(:,i) = smooth(s(:,1),3);       
    end
    Averaged(:,j) = smooth(mean(Confidence,2));
    Std(:,j) = std(Confidence,0,2);
end



%% Plotting
% plot(0:100:5000,Std(1:51,:),'LineWidth',1.2)
% figure
plot(t,Averaged,'LineWidth',1.3)
% plot(t,[Averaged(:,3)-Std(:,3), Averaged(:,3)+Std(:,3)],'--')
xlabel('DIP iterations')
ylabel('True Class Confidence')
xlim([0 5000])
% legend('Std = 1/64','Std = 1/32','Std = 1/16','Std = 1/8','Std = 1/4','Std = 1/2')
% legend('Std = 1/256','Std = 1/128','Std = 1/64','Std = 1/32');
legend('Input depth = 2','Input depth = 4','Input depth = 8','Input depth = 16','Input depth = 32','Input depth = 64')
grid on
