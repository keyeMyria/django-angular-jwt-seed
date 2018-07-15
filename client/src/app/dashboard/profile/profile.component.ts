import {Component, OnDestroy, OnInit} from '@angular/core';
import {SourceService} from '../services/';
import {ProfileModel} from '../models/profile.model';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-profile-component',
  templateUrl: 'profile.component.html',
  styles: []
})
export class ProfileComponent implements OnInit, OnDestroy {
  profile: ProfileModel | null;

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
