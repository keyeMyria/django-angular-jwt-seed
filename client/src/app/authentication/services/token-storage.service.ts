import { Injectable } from '@angular/core';

import { Observable, of as observableOf } from 'rxjs';

@Injectable()
export class TokenStorage {

  /**
   * Get access token
   * @returns {Observable<string>}
   */
  public static getAccessToken(): Observable<string> {
    const token: string = <string>localStorage.getItem('accessToken');
    return observableOf(token);
  }

  /**
   * Get refresh token
   * @returns {Observable<string>}
   */
  public static getRefreshToken(): Observable<string> {
    const token: string = <string>localStorage.getItem('refreshToken');
    return observableOf(token);
  }

  /**
   * Set access token
   * @returns {TokenStorage}
   */
  public setAccessToken(token: string): TokenStorage {
    localStorage.setItem('accessToken', token);

    return this;
  }

  /**
   * Set refresh token
   * @returns {TokenStorage}
   */
  public setRefreshToken(token: string): TokenStorage {
    localStorage.setItem('refreshToken', token);

    return this;
  }

  /**
   * Remove tokens
   */
  clear(): void {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
  }
}
