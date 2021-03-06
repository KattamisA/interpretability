clear all;
close all;

%% Original image noise
% s = load('data/orig_noisy.txt');
% Average = smooth(mean(s,2),7);
% Std = smooth(std(s,0,2),7);
% hold on
% plot(1:128,Average,'b','LineWidth',1.5)
% plot(1:128,[Average+Std, Average-Std],'--b','LineWidth',0.2,'HandleVisibility','off')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% grid on
% ylim([0,1])
% xlim([0,128])
%% Plotting for the LCCI
% load 'LCCI_[50_100].txt'
% load 'LLCI_[1_5_10_25].txt'
% LCCI_noisy = zeros(128,6);
% 
% LCCI_noisy(:,5:6) = LCCI__50_100_(:,1:2);
% LCCI_noisy(1:64,1:4) = LLCI__1_5_10_25_(:,1:4);
% 
% plot(1:64,reshape(smooth(LCCI_noisy(1:64,:),5),64,6))
% 
% xlabel('Noise standard deviation')
% ylabel('Confidence of true class')
% legend('\epsilon = 1', '\epsilon = 5', '\epsilon = 10', '\epsilon = 25', '\epsilon = 50', '\epsilon = 100')

%% Plotting for the FGSM
% load data/FGSM.txt
% 
% plot(1:128,reshape(smooth(FGSM(1:128,:),15),128,6))
% 
% xlabel('Noise standard deviation')
% ylabel('Confidence of true class')
% legend('\epsilon = 1', '\epsilon = 5', '\epsilon = 10', '\epsilon = 25', '\epsilon = 50', '\epsilon = 100')

%% Plotting the samples for FGSM
t=1:128;
Average1 = zeros(128,6);
Average2 = zeros(128,6);
Average3 = zeros(128,6);
Std = zeros(128,6);
eps = [1,5,10,25,50,100];
for i = 1:size(eps,2)
    path = sprintf('data/FGSM_eps%d.txt',eps(i));
    s = load(path);
    Average1(:,i) = mean(s,2);
    Std(:,i) = std(s,0,2);
end
for i = 1:size(eps,2)
    path = sprintf('data/BI_eps%d.txt',eps(i));
    s = load(path);
    Average2(:,i) = mean(s,2);
    Std(:,i) = std(s,0,2);
end
for i = 1:size(eps,2)
    path = sprintf('data/LLCI_eps%d.txt',eps(i));
    s = load(path);
    Average3(:,i) = mean(s,2);
    Std(:,i) = std(s,0,2);
end
hold on

k = [1,3,6];

for i = 1:3
    subplot(1,3,i)
    Average4 = smooth(Average1(:,k(i)),7);
    Average5 = smooth(Average2(:,k(i)),7);
    Average6 = smooth(Average3(:,k(i)),7);
    Std1 = smooth(Std(:,k(i)),7);
    hold on
    plot(t,Average4,'LineWidth',1.5)
    plot(t,Average5,'LineWidth',1.5)
    plot(t,Average6,'LineWidth',1.5)
%     plot(t',[Average1+Std1, Average1-Std1],'--r','LineWidth',0.2,'HandleVisibility','off')
    ylabel('True class confidence')
    xlabel('Noise standard deviation')
    title_name = sprintf('epsilon = %d',eps(k(i)));
    legend('FGSM','BI','LLCI')
    title(title_name)
    grid on
    ylim([0,1])
    xlim([0,128])
    if i>2
        ylim([0,0.5])
    end
end

for q=1:1
% load 'FGSM_eps1.txt'
% load 'FGSM_eps5.txt'
% load 'FGSM_eps10.txt'
% load 'FGSM_eps25.txt'
% load 'FGSM_eps50.txt'
% load 'FGSM_eps100.txt'
% 
% subplot(2,3,1)
% plot(1:128,FGSM_eps1,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 1')
% subplot(2,3,2)
% plot(1:128,FGSM_eps5,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 5')
% subplot(2,3,3)
% plot(1:128,FGSM_eps10,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 10')
% subplot(2,3,4)
% plot(1:128,FGSM_eps25,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 25')
% subplot(2,3,5)
% plot(1:128,FGSM_eps50,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 50')
% subplot(2,3,6)
% plot(1:128,FGSM_eps100,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 100')
end %% extra code
%% Plotting the samples for LCCI
% t=1:128;
% Average = zeros(128,6);
% Std = zeros(128,6);
% eps = [1,5,10,25,50,100];
% for i = 1:size(eps,2)
%     path = sprintf('data/LLCI_eps%d.txt',eps(i));
%     s = load(path);
%     Average(:,i) = mean(s,2);
%     Std(:,i) = std(s,0,2);
% end
% 
% for i = 1:6
%     subplot(2,3,i)
%     Average1 = smooth(Average(:,i),7);
%     Std1 = smooth(Std(:,i),7);
%     hold on
%     plot(t,Average1,'b','LineWidth',1.5)
%     plot(t',[Average1+Std1, Average1-Std1],'--b','LineWidth',0.2,'HandleVisibility','off')
%     ylabel('True class confidence')
%     xlabel('Noise standard deviation')
%     title_name = sprintf('epsilon = %d',eps(i));
%     title(title_name)
%     grid on
%     ylim([0,1])
%     xlim([0,128])
% end


for q=1:1
% load 'LLCI_eps1.txt'
% load 'LLCI_eps5.txt'
% load 'LLCI_eps10.txt'
% load 'LLCI_eps25.txt'
% load 'LLCI_eps50.txt'
% load 'LLCI_eps100.txt'
% 
% subplot(2,3,1)
% plot(1:128,LLCI_eps1,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 1')
% subplot(2,3,2)
% plot(1:128,LLCI_eps5,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 5')
% subplot(2,3,3)
% plot(1:128,LLCI_eps10,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 10')
% subplot(2,3,4)
% plot(1:128,LLCI_eps25,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 25')
% subplot(2,3,5)
% plot(1:128,LLCI_eps50,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 50')
% subplot(2,3,6)
% plot(1:128,LLCI_eps100,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 100')
end
%% Plotting the samples for BI
% t=1:128;
% Average = zeros(128,6);
% Std = zeros(128,6);
% eps = [1,5,10,25,50,100];
% for i = 1:size(eps,2)
%     path = sprintf('data/BI_eps%d.txt',eps(i));
%     s = load(path);
%     Average(:,i) = mean(s,2);
%     Std(:,i) = std(s,0,2);
% end
% 
% for i = 1:6
%     subplot(2,3,i)
%     Average1 = smooth(Average(:,i),7);
%     Std1 = smooth(Std(:,i),7);
%     hold on
%     plot(t,Average1,'b','LineWidth',1.5)
%     plot(t',[Average1+Std1, Average1-Std1],'--b','LineWidth',0.2,'HandleVisibility','off')
%     ylabel('True class confidence')
%     xlabel('Noise standard deviation')
%     title_name = sprintf('epsilon = %d',eps(i));
%     title(title_name)
%     grid on
%     ylim([0,1])
%     xlim([0,128])
%     if i>3
%         ylim([0,0.2])
%     end
% end

for q =1:1
% load 'BI_eps1.txt'
% load 'BI_eps5.txt'
% load 'BI_eps10.txt'
% load 'BI_eps25.txt'
% load 'BI_eps50.txt'
% load 'BI_eps100.txt'
% 
% subplot(2,3,1)
% plot(1:128,BI_eps1,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 1')
% subplot(2,3,2)
% plot(1:128,BI_eps5,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 5')
% subplot(2,3,3)
% plot(1:128,BI_eps10,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 10')
% subplot(2,3,4)
% plot(1:128,BI_eps25,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 25')
% subplot(2,3,5)
% plot(1:128,BI_eps50,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 50')
% subplot(2,3,6)
% plot(1:128,BI_eps100,'+')
% ylabel('True class confidence')
% xlabel('Noise standard deviation')
% title('\epsilon = 100')
end
