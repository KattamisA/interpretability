clear all
close all

img_names = ["panda", "peacock", "F16_GT", "monkey",'zebra_GT','goldfish','whale','dolphin','spider','labrador','snake','flamingo_animal','canoe','car_wheel','fountain','football_helmet','hourglass','refrigirator','knife','rope'];

common = 'Arch%d/%s_PSNR.txt';
Value = zeros(51,20);
Average = zeros(51,6);
standard_deviation = zeros(51,6);

for j=1:6
    for i=1:size(img_names,2)
        path = sprintf(common,j,img_names(i));
        s = load(path);
        Value(:,i) = smooth(s(1:51,1),3);
    end
    Average(:,j) = mean(Value,2);
    standard_deviation(:,j) = std(Value,0,2);
end

figure
plot(0:100:5000, Average, 'linewidth', 1.3)
xlabel('DIP iterations')
ylabel('PSNR')
grid on
ylim([10 32])
legend('Scenario 1','Scenario 2', 'Scenario 3', 'Scenario 4','Scenario 5 - Baseline','Scenario 6')

figure
plot(0:100:5000, standard_deviation, 'linewidth', 1)
xlabel('DIP iterations')
ylabel('PSNR standard deviation')
grid on
legend('Constant Feature Maps per layer - # parameters ~150k', 'Changing Feature Maps per layer - # parameters ~150k', 'Constant Feature Maps per layer - # parameters ~600k', 'Changing Feature Maps per layer - # parameters ~600k', 'Constant Feature Maps per layer - # parameters ~2200k (Baseline)', 'Changing Feature Maps per layer - # parameters ~2200k')
