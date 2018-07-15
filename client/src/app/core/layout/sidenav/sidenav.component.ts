import {Component} from '@angular/core';
import {ProfileModel, ProfileSourceService} from '../../../dashboard/';

import {Observable} from 'rxjs';
import {map} from 'rxjs/operators';

@Component({
  selector: 'app-sidenav-component',
  templateUrl: 'sidenav.component.html',
  styles: [``]
})
export class SidenavComponent {
  collapsed = true;

  sideMenu$: Observable<any[]>;

  constructor(private _source: ProfileSourceService) {


    this.sideMenu$ = this._source.data$
      .pipe(
        map((profile: ProfileModel) => profile.sidemenu));
  }

}
