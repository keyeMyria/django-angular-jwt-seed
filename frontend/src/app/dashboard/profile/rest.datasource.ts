import {Injectable, Inject, InjectionToken} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams, HttpRequest, HttpResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/delay';
import {BaseService} from '../../shared/_services/base.service';
import {UserProfile} from './profile.model';

@Injectable()
export class ProfileRestDataSource {

  constructor(private http: HttpClient, private _baseService: BaseService) {
  }

  getData(): Observable<UserProfile> {
    return this.http.get(this._baseService.getBaseUrl() + 'profile/') as Observable<UserProfile>;
  }
}
