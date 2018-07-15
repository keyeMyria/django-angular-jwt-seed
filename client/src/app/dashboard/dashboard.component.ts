import {Component, OnDestroy, OnInit} from '@angular/core';
import {ProfileModel} from './models/profile.model';
import {Subscription} from 'rxjs/index';
import {SourceService} from './services';

@Component({
  selector: 'app-dashboard-component',
  templateUrl: 'dashboard.component.html',
  styles: []
})
export class DashboardComponent implements OnInit, OnDestroy {
  profile: ProfileModel;

  subscription: Subscription;

  constructor(private _source: SourceService) {

    this.subscription = this._source.data$
      .subscribe((profile: ProfileModel) => this.profile = profile);
  }


  ngOnInit() {

  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
