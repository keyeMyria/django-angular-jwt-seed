import {Component, OnDestroy, OnInit} from '@angular/core';
import {MatSnackBar} from '@angular/material';

import {MessagesService} from '../../../shared/services/';

import {Subscription} from 'rxjs';

@Component({
  selector: 'app-bottom-component',
  templateUrl: 'bottom.component.html'
})
export class BottomComponent implements OnInit, OnDestroy {
  subscription: Subscription;

  constructor(public snackBar: MatSnackBar, private _msgService: MessagesService) {
    this.subscription = this._msgService.snack_notification$
      .subscribe(
        (data: any) => {
          if (!data) {
            return;
          }
          this.snackBar.open(data, 'Undo',
            {duration: 3000}
          );
        }
      );
  }

  onMessage(msg) {
    this._msgService.snack_notification$.next(msg);
  }

  ngOnInit() {
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
