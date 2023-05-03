import numpy


class AccuracyTracker(object):
    def __init__(self, n_classes):
        self.n_classes = n_classes
        self.confusion_matrix = numpy.zeros((n_classes, n_classes))

    def reset(self):
        self.confusion_matrix = numpy.zeros((self.n_classes, self.n_classes))

    def _fast_hist(self, label_true, label_pred, n_class):
        mask = (label_true >= 0) & (label_true < n_class)
        hist = numpy.bincount(
            n_class * label_true[mask].astype(int) + label_pred[mask],
            minlength=n_class**2,
        ).reshape(n_class, n_class)
        return hist

    def update(self, label_trues, label_preds):
        for lt, lp in zip(label_trues, label_preds):
            self.confusion_matrix += self._fast_hist(
                lt.flatten(), lp.flatten(), self.n_classes
            )

    def get_scores(self):
        """Returns accuracy score evaluation result.
        - overall accuracy
        - mean accuracy
        - mean IU
        - fwavacc
        """
        hist = self.confusion_matrix
        self.acc = numpy.diag(hist).sum() / hist.sum()
        acc_cls = numpy.diag(hist) / (hist.sum(axis=1) + 0.000000001)
        self.acc_cls = numpy.nanmean(acc_cls)

        with numpy.errstate(invalid='ignore'):
            dice = 2*numpy.diag(hist) / (hist.sum(axis=1) + hist.sum(axis=0))

        self.mean_dice = numpy.nanmean(dice)
        freq = hist.sum(axis=1) / hist.sum()
        self.fwavacc = (freq[freq > 0] * dice[freq > 0]).sum()
        self.cls_dice = dict(zip(range(self.n_classes), dice))

        return {
            "Overall Acc: \t": self.acc,
            "Mean Acc : \t": self.acc_cls,
            "FreqW Acc : \t": self.fwavacc,
            "Mean Dice : \t": self.mean_dice,
        }
